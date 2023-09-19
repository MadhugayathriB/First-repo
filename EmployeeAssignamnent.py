def result():
    employee_list={}
    pythonlist=[]
    javalist=[]
    devopslist=[]
    dotnetlist=[]
    testinglist=[]
    num_of_employees=int(input("Enter num of employees: "))
    for i in range(num_of_employees):
        domain=input("Enter domain: ")
        name=input("Enter name: ")
        emp_id=input("Enter emp_id: ")
        email=input("Enter mail: ")
        d={"name":name,"emp_id":emp_id,"email":email}
        if domain=="python":
            pythonlist.append(d)
            employee_list["python"]=pythonlist
        elif domain=="java":
            javalist.append(d)
            employee_list["java"]=javalist
        elif domain=="devops":
            devopslist.append(d)
            employee_list["devops"]=devopslist
        elif domain=="dotnet":
            dotnetlist.append(d)
            employee_list["dotnet"]=dotnetlist
        elif domain=="testing":
            testinglist.append(d)
            employee_list["testing"]=testinglist    
    print(employee_list)#prints entire list
    dom=input("Enter domain: ")
    print(employee_list[dom])#prints only details of one domain
    for i in employee_list[dom]:
        print(i["name"])#prints name in one domian
result()