##########################################################################################################
# Known issue : 
# 1. paramiko can't work on cryptography 2.5
#    workaround : pip install cryptography==2.4.2
# 2. Command "reboot" can't be used to send command , it should be a Absolute path , ex: /sin/reboot
##########################################################################################################

import paramiko # For SSH
import time

Test_IP = "10.162.246.26"	
Firmware_Version = "2019.03-2.0"
KeepAlive_Timeout = 60


##########################################################################################################

class SSH_Connection():

    def __init__(self,username="root",password="0penBmc",port=22):
        self.username = username
        self.password = password
        self.port = port
		
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
		
    def SSH_Open(self,ip):   
        self.client.connect(ip, port=self.port, username=self.username, password=self.password)
		
		# Transport part should be behind client.connect
        self.transport = self.client.get_transport()
        self.transport.set_keepalive(KeepAlive_Timeout)
		
    def SSH_SendCommand(self,SSH_Command):
        (stdin, stdout, stderr) = self.client.exec_command(SSH_Command) 
        Command_return = stdout.readlines()		
        return Command_return
		
    #def SSH_Ifalive(self):
    #    self.transport = self.client.get_transport()
    #    SSH_State = self.transport.isAlive()
    #    return SSH_State
		
    def SSH_Close(self):		
        self.client.close()

##########################################################################################################

SSH_Test = SSH_Connection()

def Console_Reboot(StressCount=1,ResetToDefault=False):
    for item in range(StressCount):
        SSH_Test = SSH_Connection()
        SSH_Test.SSH_Open(Test_IP)
        if ResetToDefault == False:
            SSH_Test.SSH_SendCommand("/sbin/reboot")
        else:
            SSH_Test.SSH_SendCommand("rm -rf /run/initramfs/rw/cow/*;/sbin/reboot")
        SSH_Test.SSH_Close()
		
		# Wait for BMC Reboot
        time.sleep(120)	

def SSH_Open(Test_IP):
    #SSH_Test = SSH_Connection()
    SSH_Test.SSH_Open(Test_IP)

def Send_Command(command,SSH_Test=SSH_Test):
    #SSH_Test = SSH_Connection()
    #if SSH_Test.SSH_Ifalive()==False:
    #    print("I'm reconnect")
    #    SSH_Open(Test_IP)
    #SSH_Test.SSH_Open(Test_IP)
    Command_Result = SSH_Test.SSH_SendCommand(command)   
    #SSH_Test.SSH_Close()
    return Command_Result

def SSH_Close():
    SSH_Test.SSH_Close()





##########################################################################################################

## Reboot for once without Reset to Default
#Console_Reboot() 
#
## Reboot for twice without Reset to Default
#Console_Reboot(2) 
#
## Reboot for once with Reset to Default
#Console_Reboot(ResetToDefault=True) 
#
## Reboot for twice with Reset to Default
#Console_Reboot(2,ResetToDefault=True) 
#
## System Commands

#------------------------------------------

SSH_Open(Test_IP)

Send_Command("/sbin/reboot")
time.sleep(120)	

#Send_Command("rm -rf /run/initramfs/rw/cow/*;/sbin/reboot")
#time.sleep(120)

SSH_Open(Test_IP)
firmwareversion = Send_Command("cat /etc/os-release")
print(firmwareversion)
#
#eth0_ipaddress = Send_Command("/sbin/ip addr")
#print(eth0_ipaddress)

SSH_Close()



