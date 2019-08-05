from SSH_APIs import *

##########
# APP028 #
##########
LDAP_Enable = "true"
LDAP_Server_IP = "10.162.243.203"
LDAP_Base_DN = "dc=tfb,dc=com"
LDAP_Encryption_Enable = "false"
LDAP_Client_ID = "hunk@tfb.com"
LDAP_Client_Password = "Password1"
LDAP_Permission_Attr = "description"

LDAP_Settings = [LDAP_Enable,
                 LDAP_Server_IP,
				 LDAP_Base_DN,
				 LDAP_Encryption_Enable,
				 LDAP_Client_ID,
				 LDAP_Client_Password,
				 LDAP_Permission_Attr]

LDAP_Set_Commands = ["/usr/sbin/aim_config_set_bool pam_ldap_bool_enabled ",
                     "/usr/sbin/aim_config_set_str pam_ldap_str_dc_1 ",
					 "/usr/sbin/aim_config_set_str pam_ldap_str_base_dn ",
                     "/usr/sbin/aim_config_set_bool pam_ldap_bool_encryption_enabled ",
                     "/usr/sbin/aim_config_set_str pam_ldap_str_client_id ",
                     "/usr/sbin/aim_config_set_str pam_ldap_str_client_password ",
                     "/usr/sbin/aim_config_set_str pam_ldap_str_login_permission_attr "]

LDAP_Get_Commands = ["/usr/sbin/aim_config_get_bool pam_ldap_bool_enabled",
                     "/usr/sbin/aim_config_get_str pam_ldap_str_dc_1",
					 "/usr/sbin/aim_config_get_str pam_ldap_str_base_dn",
                     "/usr/sbin/aim_config_get_bool pam_ldap_bool_encryption_enabled",
                     "/usr/sbin/aim_config_get_str pam_ldap_str_client_id",
                     "/usr/sbin/aim_config_get_str pam_ldap_str_client_password",
                     "/usr/sbin/aim_config_get_str pam_ldap_str_login_permission_attr"]

def APP028_0000():					 
    for item in range(len(LDAP_Set_Commands)):
        SSH_Write(LDAP_Set_Commands[item] + LDAP_Settings[item])
        delays(1,LDAP_Set_Commands[item])
        Command_Response=SSH_Write(LDAP_Get_Commands[item])
        print(Command_Response)
        if Command_Response[0]==LDAP_Settings[item]:
            print("Pass")
        else:
            print("Fail")

    return "Pass"

def APP028_0001():
    Test_Title = "Test Authentication with wrong LDAP_Client_ID" 
    Wrong_LDAP_Client_ID = "hunk2@tfb.com"
    SSH_Read_Until("checkUser user="+Wrong_LDAP_Client_ID,"Password:",5)
    test_result=SSH_Read_Until(LDAP_Client_Password,"Authorized",5)
	
    #print(test_result)
    if test_result.find('Authorized') < 0:
        print(Test_Title+" : Pass")
        return "Pass"
    else:
        print(Test_Title+" : Fail")	
        return "Fail"

def APP028_0002():
    Test_Title = "Test Authentication with wrong LDAP_Client_Password"
    Wrong_LDAP_Client_Password = "Password2"
    SSH_Read_Until("checkUser user="+LDAP_Client_ID,"Password:",5)
    test_result=SSH_Read_Until(Wrong_LDAP_Client_Password,"Authorized",5)
	
    #print(test_result)
    if test_result.find('Authorized') < 0:
        print(Test_Title+" : Pass")
        return "Pass"
    else:
        print(Test_Title+" : Fail")	
        return "Fail"

def APP028_0003():
    Test_Title = "Test Authentication with correct LDAP_Client_ID and LDAP_Client_Password"
    SSH_Read_Until("checkUser user="+LDAP_Client_ID,"Password:",5)
    test_result=SSH_Read_Until(LDAP_Client_Password,"Authorized",30)

    #print(test_result)
    if test_result.find('Authorized') > 0:
        print(Test_Title+" : Pass")
        return "Pass"
    else:
        print(Test_Title+" : Fail")	
        return "Fail"