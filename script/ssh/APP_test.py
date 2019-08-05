from SSH_APIs import *
from SSH_Log import *

def APP_test_01():
    TestTitle("APP031_0001")
    print("APP_test_01")
    test = 0 
    if test > 0 :
        return "Fail"
    else:
        return "Pass"
    
def APP_test_02():
    TestTitle("APP_test_02")
    print("APP_test_02")	
    test = 1 
    if test > 0 :
        return "Fail"
    else:
        return "Pass"
