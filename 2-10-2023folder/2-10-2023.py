#calculator function
from calculatorfunctions import *
print("For addition: add")
print("For substraction; sub")
print("For multiplication: mul")
print("For division: div")
cal=input("Enter req calculator: ")
if cal=="add":
    add(1,2,3,4,5)
elif cal=="sub":
    sub(1,2,3,4,5)
elif cal=="mul":
    mul(1,2,3,4,5)
elif cal=="div":
    div(1,2,3,4,5)

#2 filter employee 
n=int(input("Enter no.of employees: "))
emp_details={}
for i in range(1,n+1):
    name=input("Enter name: ")
    designation=input("Enter designation: ")
    emp_id=input("Enter emp.id: ")
    email=input("Enter email: ")
    emp_details[name]={"name":name,"email":email,"designation":designation,"emp_id":emp_id}
des=input("Enter designation: ")
def find(i):
    v=emp_details[i]
    if v["designation"]==des:
            return v
res=list(filter(find,emp_details))
print(res)

