#1 first prblm : positive r negative 
num=24 
if num%2==0:
    print("Its a positive number")
else:
    print("Its a negative number")

num =75
if num%2==0:
    print("The num is divisible by 2 so its a positive number")
else:
    print("The number is divisible by 2 so its a negative number")

num=11
if num%2==0:
    print("Its Positive")
else:
    print("Its Negative")

num=157
if num%2==0:
    print("Num leaves a remainder 0 so its even number")
else:
    print("Num leaves remainder 1 so num is odd ")

num =93
if num%2==0:
    print("Its positive")
else:
    print("Its negative")


#2 second problrm : find greater number
a=56
b=78
if a>b:
    print(str(a) +"is greater than "+ str(b))
else:
    print(str(b) +" is greater than "+ str(a))

a=128
b=985
if a>b:
    print(str(a) +"is bigger number")
else:
    print(str(b) +" is bigger number ")

li=[5,8,9,11,17]
first=li[0]
greater=first
for i in li:
    if i>greater:
        greater=i
print(greater)

a=45
b=90
if a<b:
    print(str(a) +" is smaller than b")
else:
    print(str(b) +" is smaller than a")