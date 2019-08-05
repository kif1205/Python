TestResult = []

Import_Modules = ["APP028","APP031"]

for item in Import_Modules:
    exec("import "+item) 

for TestModuleName in Import_Modules:
    AllFunctions = eval("dir(" + TestModuleName + ")")	
    for item in AllFunctions:
        if item.find(TestModuleName)==0:
            TestResult.append(eval(TestModuleName+"."+item+"()"))

Pass_Count = 0
Fail_Count = 0

for item in TestResult:
    if item == "Pass":
        Pass_Count+=1
    if item == "Fail":
        Fail_Count+=1

print("\n\nPass : ",Pass_Count)
print("Fail : ",Fail_Count)






























