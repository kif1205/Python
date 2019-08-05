import paramiko
import time

def SSH_Init(Test_IP,Test_Port,Test_UserName,Test_Password):

    global client
    global BMC_SSH_IP 
    global BMC_SSH_UserName
    global BMC_SSH_PassWord
    global BMC_SSH_Port

    BMC_SSH_IP = Test_IP
    BMC_SSH_Port = Test_Port
    BMC_SSH_UserName = Test_UserName
    BMC_SSH_PassWord = Test_Password
	
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    client.connect(BMC_SSH_IP, port=BMC_SSH_Port, username=BMC_SSH_UserName, password=BMC_SSH_PassWord)
			
			
SSH_Init_IP="10.162.246.249"
SSH_Init_Port="22"
SSH_Init_UserName="root"
SSH_Init_Password="0penBmc"

Service_UserName="admin"
Service_Password="Password1"

SSH_Init(SSH_Init_IP,SSH_Init_Port,SSH_Init_UserName,SSH_Init_Password)

stdin, stdout, stderr = client.exec_command('checkUser user=hunk@tfb.com')
stdin.write("Password")
stdin.write("\n")
stdin.flush()
Command_return = stdout.readlines()	
print(Command_return)

		