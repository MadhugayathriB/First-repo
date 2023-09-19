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

# def result():
#     Employeedetails={}
#     Number_of_employees=int(input("Enter_num_of_employees: "))
#     for i in range(1,Number_of_employees+1):
#         name=input("Name_of_employee: ")
#         domain=input("Employee_domain: ")
#         emp_id=input("Enter emp_id: ")
#         email_id=input("Enter_mailid: ")
#         Employeedetails[i]={"name":name,"domain":domain,"emp_id":emp_id,"email_id":emp_id}
#     print(Employeedetails)
#     dom=input("Enter domain: ")
#     for k,v in Employeedetails.items():
    
#         if v["domain"]==dom:
#             print(v)
# result()