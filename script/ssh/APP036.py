from SSH_APIs import *

"""
root@blueplate-ast2500evb:~# cat -n /etc/blueplate/blueplate_z51_hostinterface.conf
     1  {
     2    "/redfish/v1/Managers/bmc/HostInterfaces/1": {
     3      "ManagerEthernetInterface": {
     4  "@odata.id": "/redfish/v1/Managers/bmc/EthernetInterfaces/eth0"
     5      }
     6    },
     7    "/redfish/v1/Managers/bmc/HostInterfaces/1/HostEthernetInterfaces": {
     8      "Members": [
     9        {
    10          "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/ToManager"
    11        }
    12      ]
    13    },
    14  "/redfish/v1/Managers/bmc/EthernetInterfaces/eth0": {
    15      "IPv4Addresses": [
    16        {
    17  "Address": "10.162.244.44",
    18  "SubnetMask": "255.255.248.0",
    19          "AddressOrigin": "Static",
    20  "Gateway": "10.162.240.1"
    21        }
    22      ]
    23    },
    24    "/redfish/v1/Systems/1/EthernetInterfaces/ToManager": {
    25      "IPv4Addresses": [
    26        {
    27  "Address": "10.162.246.5",
    28  "SubnetMask": "255.255.248.0",
    29          "AddressOrigin": "Static",
    30  "Gateway": "10.162.240.1"
    31        }
    32      ]
    33    }
    34  }
"""

"""
root@blueplate-ast2500evb:~# cat -n /usr/local/etc/nginx/AuthNoneMode.conf
     1  ##  This file is the configuration of the AuthNone mode.
     2  ##  The config is stored as key=value pair
     3  ##  If the value is empty, the key will be delete.
     4
     5  # HostIPAddress is the IP address of Redfish Host Interface.
     6  # IPv4 and IPv6 are supported.
     7  # Default value: none
     8  HostIPAddress=
     9
    10  # AuthNonePrivileges is a number of combined privileges.
    11  # For example,
    12  #   An expected priviles contains "Login" and "ConfigureComponents"
    13  #   Refer to privileges.conf definitions, the value is 0x0001 + 0x0010 = 0x0011
    14  # Default value: none
    15  AuthNonePrivileges=
    16
    17  # HostInterfaceProxyOrigin is a token of the HostInterface proxy.
    18  # This is optional if a proxy is setup.
    19  # The proxy should append this token to the request header "X-Origin".
    20  # Default value: none
    21  HostInterfaceProxyOrigin=LocalHIProxy
"""

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
command = "/bin/sed -i '8c HostIPAddress=10.162.246.5' /usr/local/etc/nginx/AuthNoneMode.conf"
SSH_Write(command)

command = "/bin/sed -i '15c AuthNonePrivileges=0x1ff' /usr/local/etc/nginx/AuthNoneMode.conf"
SSH_Write(command)

SSH_Write("/bin/systemctl restart nginx blueplate_z51_hostinterface")

print(SSH_Write("/bin/cat /etc/blueplate/blueplate_z51_hostinterface.conf"))	
