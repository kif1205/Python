##########################################################################################################
# Known issue : 
# 1. paramiko can't work on cryptography 2.5
#    workaround : pip install cryptography==2.4.2
# 2. Command "reboot" can't be used to send command , it should be a Absolute path , ex: /sin/reboot
##########################################################################################################

from SSH_Driver import *

def SSH_Init():
	
    global SSH_Test
    SSH_Test = SSH_Connection()

    global SSH_IP 
    global SSH_UserName
    global SSH_Password
    global SSH_Port
	
    SSH_Settings=[]	
    f = open("SSH_config.ini", "r")
    for x in f:
        SSH_Settings.append(x.split("=")[1])
    
    SSH_IP = str(SSH_Settings[0][:-1])
    SSH_UserName = str(SSH_Settings[1][:-1])
    SSH_Password = str(SSH_Settings[2][:-1])
    SSH_Port = int(SSH_Settings[3])

    SSH_Test.settings(SSH_IP,SSH_UserName,SSH_Password,SSH_Port)	
    SSH_Test.open()
	
def SSH_Write(command):

    timeout_count = 3

    while timeout_count > 0:	
        try:
            #print("##### SSH Write Try")
            print(command)		
            return SSH_Test.send(command)
	    
        except (AttributeError, paramiko.ssh_exception.SSHException) as exception_reason:
            #print("##### SSH Write Exception")
            print("Exception reason is : ",exception_reason)
            SSH_Test.open()
         
        timeout_count-=1
	
def delays(seconds,delay_reason=""):

    print(delay_reason)
    while seconds >= 0:
        time.sleep(1)        
        second_str = "%d seconds...\r" %seconds
        print(second_str, end='')
        seconds -= 1

# SSH_Read_Until()
# Command : Send Command
# Output_Data : What message will be found after sending Command 
def SSH_Read_Until(Command,Output_Data,TimeOut=30):	

    timeout_count = 3
	
    while timeout_count > 0:	
	
        try:
            return SSH_Test.send_until(Command,Output_Data,TimeOut)
	    			    	
        except (AttributeError, paramiko.ssh_exception.SSHException) as exception_reason:
            print("Exception reason is : ",exception_reason)
            SSH_Test.open()
					
        timeout_count-=1

def SSH_Config_ReplaceOneLine(test_dict,configfile):
    for key,value in test_dict.items():
        command = "sed -i '"+key+"c"+value+"' "+configfile
        print(command)
        SSH_Write(command)   

def SSH_Config_Insert(test_dict,configfile):
    for key,value in test_dict.items():
        command = "sed -i '"+key+"i"+value+"' "+configfile
        print(command)
        SSH_Write(command)   
		
# DBus_Command : What DBus Command do you want to send 
# Query_Parameters : { "property name" : "expected data" }
#                     - property name : String Type 
#                     - expected data : String Type 
def SSH_DBus_Verify(DBus_Command,Query_Parameters):
  
    Dbus_result = SSH_Write(DBus_Command) 

    for key,value in Query_Parameters.items():
        for item in Dbus_result:
            if key in item:
                sub_item = item.split(" ") # Avoid the property name include expected data
                if value in sub_item:
                    print("%s is %s : Pass"%(key,value))
                    break 
                else:
                    print("%s is %s : Fail"%(key,value))

					
if __name__ == 'SSH_APIs':
    SSH_Init()

