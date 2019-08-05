from SSH_APIs import *

BMC_IP = "10.162.244.44"
BMC_Mask = "255.255.248.0"
BMC_GateWay = "10.162.240.1"

Client_IP = "10.162.246.5"
Client_Mask = "255.255.248.0"
Client_GateWay = "10.162.240.1"

blueplate_z51_hostinterface_configfile = "/etc/blueplate/blueplate_z51_hostinterface.conf"
AuthNoneMode_configfile = "/usr/local/etc/nginx/AuthNoneMode.conf"

def APP036_00000():
    test_dict = { "3" : '"FirmwareAuthEnabled":true,',
                  "4" : '"KernelAuthEnabled":true,'}
    SSH_Config_Insert(test_dict,blueplate_z51_hostinterface_configfile)
    
    
    test_dict = { "6"  : '"@odata.id": "/redfish/v1/Managers/bmc/EthernetInterfaces/eth0"' ,
                  "16" : '"/redfish/v1/Managers/bmc/EthernetInterfaces/eth0": {' ,
                  "19" : '"Address": "'+BMC_IP+'",' ,
                  "20" : '"SubnetMask": "'+BMC_Mask+'",' ,
                  "22" : '"Gateway": "'+BMC_GateWay+'"' ,
                  "29" : '"Address": "'+Client_IP+'",',
                  "30" : '"SubnetMask": "'+Client_Mask+'",',
                  "32" : '"Gateway": "'+Client_GateWay+'"'			  
    			  }
    SSH_Config_ReplaceOneLine(test_dict,blueplate_z51_hostinterface_configfile)
    
    test_dict = { "8" : "HostIPAddress="+Client_IP,
                  "15" : "AuthNonePrivileges=0x1ff"}
    SSH_Config_ReplaceOneLine(test_dict,AuthNoneMode_configfile)
    
    print(SSH_Write("/bin/systemctl restart nginx blueplate_z51_hostinterface"))

def case2():

    Dbus_command = "busctl introspect com.vertivco.remotepresence /com/vertivco/remotepresence/videorecording/Settings --no-page"
    Query_Parameters = { "BootCaptureEnabled" : "true" ,
                         "CrashCaptureEnabled" : "false" ,
	                     "NumBootCaptureFiles" : "0",	
	                     "NumCrashCaptureFiles" : "0"						 
}	
    SSH_DBus_Verify(Dbus_command,Query_Parameters)

def case3():
    result = SSH_Write("redis-cli -s /tmp/redis.sock hgetall HostInterfaceAutoCredential")
    print(result)
    for item in range(len(result)):
        if "KernelAuthUserName" in result[item]:
            KernelAuthUserName = result[item+1]
        elif "KernelAuthPassword" in result[item]:
            KernelAuthPassword = result[item+1] 
        elif "FWAuthUserName" in result[item]:
            FWAuthUserName = result[item+1] 
        elif "FWAuthPassword" in result[item]:
            FWAuthPassword = result[item+1] 
			
    print(KernelAuthUserName)
    print(KernelAuthPassword)
    print(FWAuthUserName)
    print(FWAuthPassword)

def case4():
    configfile = "/usr/local/share/z51backend_sdata/schemas/registries/AvocentBiosAttributeRegistry.1.0.0.json/index.json"
	
	# Unspecified , Static , DynamicBmcDhcp , DynamicBmcNonDhcp
    test_dict = { "490" : '"CurrentValue": "DynamicBmcNonDhcp",'}
    SSH_Config_ReplaceOneLine(test_dict,configfile)
	
def case5():
    SSH_Write("/bin/touch /etc/bios_applied.json")

    SSH_Write("/bin/echo "+'{"Messages": [{"RelatedProperties": ["#/Attributes/EmbeddedSata"],"MessageId": "Base.1.4.PropertyValueModified"},{"RelatedProperties": ["#/Attributes/BootMode"],"MessageId": "Base.1.4.Success"}]}'+" > /etc/bios_applied.json")

	
APP036_00000()
"""
{
    "Messages": [
        {
            "RelatedProperties": [
                "#/Attributes/EmbeddedSata"
            ],
            "MessageId": "Base.1.4.PropertyValueModified"
        },
        {
            "RelatedProperties": [
                "#/Attributes/BootMode"
            ],
            "MessageId": "Base.1.4.Success"
        }
    ]
}
"""