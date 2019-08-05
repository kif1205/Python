import paramiko
import time
import re

BMC_SSH_IP='10.162.244.34'
BMC_SSH_Port=22
BMC_SSH_UserName="root"
BMC_SSH_PassWord="0penBmc"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
ssh.connect(BMC_SSH_IP, port=BMC_SSH_Port, username=BMC_SSH_UserName, password=BMC_SSH_PassWord)
	
chan = ssh.invoke_shell()

passw = "Password1"

def run_cmd(cmd):


    chan.send(cmd + '\n')

	
    buff = ''


    while buff.find('Password:') < 0:
        resp = str(chan.recv(9999))
        buff = buff + resp
    print(buff)
    buff = ''	
    chan.send(passw + '\n')

    time.sleep(20)

    resp = str(chan.recv(9999))
    buff = resp



    print(buff)
    if buff.find('Authorized') > 0:
        print("Authentication successful!")
    else:
        print("Authentication failed!")

    	

    ssh.close()




cmd="checkUser user=hunk@tfb.com"
print('\n test 2\n cmd %s\n' % cmd)
run_cmd(cmd)