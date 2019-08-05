from SSH_APIs import *
import shutil
import os

###############
#Command Pool #
###############
# Common Commands 
Common_Command_1 = "/sbin/ip addr"
Common_Command_2 = "cat /etc/os-release"
Common_Command_3 = "/sbin/reboot"


# IPMITool Commands 
IPMITool_Command_1 = "/usr/sbin/ipmitool raw 0x0a 0x44 0x00 0x00 0x02 0x00 0x00 0x00 0x00 0x20 0x00 0x04 0x07 0xa0 0x6f 0x02 0x00 0x01"
#IPMITool_Command_2 = "/usr/sbin/ipmitool -I lanplus -H " + SSH_Init_IP + " -U " + Service_UserName + " -P " + Service_Password + " -C 3 raw 6 1"
IPMITool_Command_3 = "/usr/sbin/ipmitool raw 6 1"


# Dbus Commands 
Dbus_Command_1 = "busctl introspect xyz.openbmc_project.Hwmon-2323379361.Hwmon1 /xyz/openbmc_project/sensors/temperature/blueplate_temp1 --no-page"

# Query Commands 
Query_Command_1 = "/bin/ls -al /tmp/bsod"


#print("BUILD_ID is :",SSH_FWVersion_BuildID())
#print("Eth0's IP is :",SSH_IPAddr_Eth0_IP())


#SSH_Write("/sbin/reboot")
#delays(120,"Reboot...")
#print(SSH_Write("/sbin/ip addr"))


#shutil.rmtree('./__pycache__/',ignore_errors=True)
#os.mkdir('./__pycache__/')

print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))

# /bin/sed -i '17c "Address": "10.162.244.44",' /etc/blueplate/blueplate_z51_hostinterface.conf

command = "/bin/sed -i '4c \"@odata.id\": \"\/redfish\/v1\/Managers\/bmc\/EthernetInterfaces\/eth0\"' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '14c \"\/redfish\/v1\/Managers\/bmc\/EthernetInterfaces\/eth0\": \{' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '17c \"Address\": \"10.162.244.44\",' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '18c \"SubnetMask\"\: \"255.255.248.0\",' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '20c \"Gateway\": \"10.162.240.1\"' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '27c \"Address\"\: \"10.162.246.5\"\,' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '28c \"SubnetMask\"\: \"255.255.248.0\",' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)

command = "/bin/sed -i '30c \"Gateway\": \"10.162.240.1\"' /etc/blueplate/blueplate_z51_hostinterface.conf"
SSH_Write(command)


# /usr/local/etc/nginx/AuthNoneMode.conf




print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))	