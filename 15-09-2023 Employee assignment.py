Employeedetails={}
domain_list=["python","java","devops","testing"".net"]
Number_of_employees=int(input("Enter_num_of_employees: "))
for i in range(Number_of_employees):
    name=input("Name_of_employee: ")
    domain=input("Employee_domain: ")
    emp_id=(input("Enter emp_id: "))
    email_id=input("Enter_mailid: ")
    if domain in domain_list and email_id.endswith("@gmail.com"):

        Employeedetails[name]={"domain":domain,"emp_id":emp_id,"email_id":emp_id}
    else:
        print("Enter valid details")
print(Employeedetails)



