import paramiko
import time
import socket

class SSH_Connection():

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    client_interactive = None 

    def settings(self,ip,username,password,port):	
	
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
		
    def open(self): 
	
        try:
            self.client.connect(self.ip, port=self.port, username=self.username, password=self.password,timeout=20)
            self.client_interactive = self.client.invoke_shell()

        except Exception as exception_reason:
            print("Exception reason is : ",exception_reason)
     				
    def send(self,SSH_Command):
	
        try:
            (stdin, stdout, stderr) = self.client.exec_command(SSH_Command, timeout=60) 
            Command_return = stdout.readlines()		
            return Command_return

        except socket.timeout:
            print("Exception reason is : Timeout")
			
    def send_until(self,Command,Output_Data,send_until_timeout):

        self.client_interactive.settimeout(send_until_timeout)

        try:
            self.client_interactive.send(Command + '\n')
            Receive_Buffer = ''
            		
            while Receive_Buffer.find(Output_Data) < 0:
                resp = str(self.client_interactive.recv(9999))
                Receive_Buffer = Receive_Buffer + resp
				
            #print("##### Try Receive_Buffer #####")
            #print(Receive_Buffer)	        
            return Receive_Buffer
		
        except socket.timeout:
            print("Exception reason is : Timeout")
            #print("##### Timeout Receive_Buffer #####")
            #print(Receive_Buffer)
            return Receive_Buffer