from SSH_APIs import *
import paramiko

#SSH_Write("/bin/cp /etc/miniupnpd/miniupnpd.conf /tmp/miniupnd.conf.backup")
#OriginalData = SSH_Write("/bin/cat /etc/miniupnpd/miniupnpd.conf")
#print(OriginalData)

#print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))
#for item in range(len(OriginalData)):
#    
#    temp = OriginalData[item]
#    print(temp)
#    if OriginalData[item].find("notify_interval") == 0:
#
#        temp=OriginalData[item].replace("interval=60","interval=10")
#        break
#    #print(temp)
#    temp=temp.rstrip()
#    print("/bin/echo -e '"+temp+"' > /tmp/test222")

#SSH_Write("/bin/sed -i 's/interval=60/interval=10/g' /etc/miniupnpd/miniupnpd.conf")
#SSH_Write("/bin/sed -i 's/interval=10/interval=20/g' /etc/miniupnpd/miniupnpd.conf")		

#SSH_Write("/bin/sed -i 's/"+"/redfish/v1/Managers/bmc/EthernetInterfaces/eth1"+"/"+"/redfish/v1/Managers/bmc/EthernetInterfaces/usb0"+"/g' /etc/blueplate/blueplate_z51_hostinterface.conf")

#print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))


# sed -i 's/"/redfish/v1/Managers/bmc/EthernetInterfaces/eth1"/"+"/redfish/v1/Managers/bmc/EthernetInterfaces/usb0"+"/g' /etc/blueplate/blueplate_z51_hostinterface.conf

#olddata = "\/redfish\/v1\/Managers\/bmc\/EthernetInterfaces\/eth1"
#newdata = "\/redfish\/v1\/Managers\/bmc\/EthernetInterfaces\/usb2"
#changefile = "/etc/blueplate/blueplate_z51_hostinterface.conf"
#mycommand =  "sed -i 's/" + olddata + "/" + newdata + "/g' " + changefile
#print( "sed -i 's/" + olddata + "/" + newdata + "/g' " + changefile)
#SSH_Write(mycommand)

#sed -i 's/"{\n \"\/redfish\/v1\/Managers\/bmc\/HostInterfaces\/1\""/"{\n \"\/redfish\/v1\/Managers\/bmc\/HostInterfaces\/2\""/g' /etc/blueplate/blueplate_z51_hostinterface.conf

OriginalData=SSH_Write("/bin/cat /tmp/test")
#print(OriginalData)

for item in range(len(OriginalData)):
    
    if OriginalData[item].find('"/redfish/v1/Managers/bmc/EthernetInterfaces/usb0": {') > 0:

        print(item)
        break

# 0 base

def Hostinterface_Conf_Change_Connect_IP(New_IP_Address):
    File_Change_Line = 16 		
    test=OriginalData[File_Change_Line].split('"')
    print(test[3])
    olddata=test[3]
    newdata=New_IP_Address
    command="/bin/sed -i '"+str(File_Change_Line+1)+"s/"+olddata+"/"+newdata+"/p' /tmp/test"
    SSH_Write(command)
    
    delays(1)
    
    command="/bin/sed -i '"+str(File_Change_Line+2)+"d' /tmp/test"
    SSH_Write(command)

Hostinterface_Conf_Change_Connect_IP("10.162.244.88")


# sed example
# cp /etc/blueplate/blueplate_z51_hostinterface.conf /tmp/test
# sed -i '17s/192.168.0.23/192.168.0.24/p' test
# sed -n '17s/192.168.0.10/192.168.0.22/p' test
# sed -i '18d' test
# cat -n test


# sed -i '123c\notify_interval=10' test2

print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))

# /bin/sed -i '17c "Address": "10.162.244.44",' /etc/blueplate/blueplate_z51_hostinterface.conf
command = "/bin/sed -i '17c \"Address\": \"10.162.244.44\",' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)
print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))