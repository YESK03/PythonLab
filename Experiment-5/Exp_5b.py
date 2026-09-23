def EmpCalc():
    Name = input("Enter Name")
    Age = int(input("Enter Age"))
    sal = float(input("Enter Salary"))
    HRA = (sal * 35)/100
    PF = (sal * 25)/100
    Netsal = sal + HRA + PF
    
    if (Netsal >= 30000) and (Netsal <= 100000):
        print("Senior Manager")
    elif (Netsal >= 20000) and (Netsal <= 29999):
        print("Manager")
    else:
        print("Front Level Job")
    return Name, Age, Netsal

Name, Age, Netsal = EmpCalc()
print("Employee Name:",Name)
print("Employee Age",Age)
print("Employee Net Salary",Netsal)