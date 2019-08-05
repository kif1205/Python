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
chan.settimeout(5)


def run_cmd(cmd):


    chan.send(cmd + '\n')
    time.sleep(2)
	
    buff = ''


    while buff.find('OpenSSL>') < 0:
        resp = str(chan.recv(9999))
        buff = buff + resp
    print(buff)

	
    buff = ''	
    chan.send("test" + '\n')
    
    while buff.find('desx2') < 0:
        resp = str(chan.recv(9999))
        buff = buff + resp
    print(buff)
    

    	

    ssh.close()




cmd="openssl"
print('\n test 2\n cmd %s\n' % cmd)
run_cmd(cmd)