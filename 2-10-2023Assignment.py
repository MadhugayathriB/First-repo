#calculator function
def add(*var):
    sum=0
    for i in var:
        sum=sum+int(i)
    print(sum)
def sub(*var):
    sub=0
    for i in var:
        sub=int(i)-sub
    print(sub)
def mul(*var):
    mul=1
    for i in var:
        mul=mul*int(i)
    print(mul)
def div(*var):
    div=1
    for i in var:
        div=int(i)/div
    print(div)
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
    emp_id=input("Enter emp.id: ")
    designation=input("Enter designation: ")
    email=input("Enter email: ")
    emp_details[name]={"name":name,"email":email,"designation":designation,"emp_id":emp_id}
des=input("Enter designation: ")
def find(i):
    v=emp_details[i]
    if v["designation"]==des:
            return v
res=list(filter(find,emp_details))
print(res)

