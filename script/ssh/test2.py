import time
 

Time_Start = time.time()
Timeout = 20 

if time.time() > (Time_Start+Timeout):
    print("Time out")