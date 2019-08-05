from SSH_APIs import *

##########
# APP031 #
##########
"""
- Boot&Crash Capture 

Enable/Disable Boot Capture 
    aim_config_set_bool pm_bool_capture_boot_sequence true
    aim_config_set_bool pm_bool_capture_boot_sequence false

Enable/Disable Crash Capture 
    aim_config_set_bool pm_bool_enable_crash_video_capture true
    aim_config_set_bool pm_bool_enable_crash_video_capture false

Use DBus command to check Boot/Crash Capture state
    busctl introspect com.vertivco.remotepresence /com/vertivco/remotepresence/videorecording/Settings --no-page

Enable continuous recording
    aim_config_set_bool pm_bool_enable_continuous_recording true

Start/Stop the bootcapture
    aim_send_event event_server_boot_start
    aim_send_event event_server_boot_stop
	
Get a Crash Capture 
    aim_send_event  event_server_crash
"""

APP_031_Command_BootCapture_Enable = "/usr/sbin/aim_config_set_bool pm_bool_capture_boot_sequence true"
APP_031_Command_BootCapture_Disable = "/usr/sbin/aim_config_set_bool pm_bool_capture_boot_sequence false"
APP_031_Command_BootCapture_Status = "/usr/sbin/aim_config_get_bool pm_bool_capture_boot_sequence"

APP_031_Command_CrashCapture_Enable = "/usr/sbin/aim_config_set_bool pm_bool_enable_crash_video_capture true"
APP_031_Command_CrashCapture_Disable = "/usr/sbin/aim_config_set_bool pm_bool_enable_crash_video_capture false"
APP_031_Command_CrashCapture_Status = "/usr/sbin/aim_config_get_bool pm_bool_enable_crash_video_capture"

APP_031_Command_ContinuousRecording_Enable = "/usr/sbin/aim_config_set_bool pm_bool_enable_continuous_recording true"
APP_031_Command_ContinuousRecording_Disable = "/usr/sbin/aim_config_set_bool pm_bool_enable_continuous_recording false"
APP_031_Command_ContinuousRecording_Status = "/usr/sbin/aim_config_get_bool pm_bool_enable_continuous_recording"

APP_031_Command_Start_BootCapture = "/usr/sbin/aim_send_event event_server_boot_start"
APP_031_Command_Stop_BootCapture = "/usr/sbin/aim_send_event event_server_boot_stop"
APP_031_Command_Get_CrashCapture = "/usr/sbin/aim_send_event  event_server_crash"



def APP031_0001():
    Test_Title = "Verify BootCapture is enabled"
    
    SSH_Write(APP_031_Command_BootCapture_Enable)  
    SSH_Write(APP_031_Command_ContinuousRecording_Enable) 
    SSH_Write(APP_031_Command_Start_BootCapture) 
    delays(3,"Wait for Bootcapture recording...")
    SSH_Write(APP_031_Command_Stop_BootCapture) 
    delays(3,"Wait for saving the capture file...")
    Test_Result = (SSH_Write("/bin/ls /tmp/bootcapture"))  

    Stat_Result = SSH_Write("/bin/stat /tmp/bootcapture/"+Test_Result[0])

    try:
        FileSize=Stat_Result[1].split(" ")[3]	
        
        if Test_Result[0].find("tcapture_") > 0 and int(FileSize) >0:
            print(Test_Title+" : Pass")
            return "Pass"
        else:
            print(Test_Title+" : Fail")
            return "Fail"
    except:
        print(Test_Title+" : Fail")
        return "Fail"
		
def APP031_0002():
    Test_Title = "Verify BootCapture is disabled"
    
    SSH_Write(APP_031_Command_BootCapture_Disable) 
    SSH_Write(APP_031_Command_ContinuousRecording_Enable) 
    SSH_Write(APP_031_Command_Start_BootCapture) 
    delays(3,"Wait for Bootcapture recording...")
    SSH_Write(APP_031_Command_Stop_BootCapture) 
    Test_Result = (SSH_Write("/bin/ls -al /tmp/bootcapture"))  	
		
    if Test_Result[-1].find("tcapture_") < 0:
        print(Test_Title+" : Pass")
        return "Pass"
    else:
        print(Test_Title+" : Fail")	
        return "Fail"

def APP031_0003():		
    Test_Title = "Verify CrashCapture is enabled"
	
    SSH_Write(APP_031_Command_BootCapture_Enable)  
    SSH_Write(APP_031_Command_CrashCapture_Enable)  
    SSH_Write(APP_031_Command_ContinuousRecording_Enable)  
    delays(3,"Wait for CrashCapture recording...")
    SSH_Write(APP_031_Command_Get_CrashCapture) 
    delays(3,"Wait for saving the capture file...")
	
    Test_Result = (SSH_Write("/bin/ls /tmp/crashcapture"))  
      
    try:
        Stat_Result = SSH_Write("/bin/stat /tmp/crashcapture/"+Test_Result[0])
        FileSize=Stat_Result[1].split(" ")[3]	
        
        if Test_Result[0].find("video_") > 0 and int(FileSize) >0:
            print(Test_Title+" : Pass")
            return "Pass"
        else:
            print(Test_Title+" : Fail")
            return "Fail"
    except:
        print(Test_Title+" : Fail")
        return "Fail"
		
def APP031_0004():
    Test_Title = "Verify CrashCapture is disabled"

    SSH_Write(APP_031_Command_CrashCapture_Disable) 
    SSH_Write(APP_031_Command_ContinuousRecording_Disable) 
    delays(3,"Wait for CrashCapture recording...")
    SSH_Write(APP_031_Command_Get_CrashCapture) 
    delays(3,"Wait for saving the capture file...")

    Test_Result = (SSH_Write("/bin/ls -al /tmp/crashcapture"))  	
	
    if Test_Result[-1].find("video_") < 0:
        print(Test_Title+" : Pass")
        return "Pass"
    else:
        print(Test_Title+" : Fail")	
        return "Fail"
	
def APP031_0005():
    Test_Title = "Verify CrashCapture Picture is enabled"
	
    SSH_Write(APP_031_Command_CrashCapture_Enable)     
    SSH_Write(APP_031_Command_Get_CrashCapture) 
    delays(3,"Wait for saving the capture file...")
    Test_Result = (SSH_Write("/bin/ls /tmp/bsod"))  	

    try:
	
        Stat_Result = SSH_Write("/bin/stat /tmp/bsod/bsod.png")
        FileSize=Stat_Result[1].split(" ")[3]	
        
        if Test_Result[0].find("od.png") > 0 and int(FileSize) >=0:
            print(Test_Title+" : Pass")
            return "Pass"
        else:
            print(Test_Title+" : Fail")	
            return "Fail"
    except:
        print(Test_Title+" : Fail")
        return "Fail"		














