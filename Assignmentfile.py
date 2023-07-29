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


a=67
b=67
if a>b:
    print(str(a)+" is greater than "+str(b))
elif a==b:
    print("both"+ str(a)+ "and"+ str(b) +" are equal")
else:
    print(str(b)+" is greater than "+str(a))


#3 third problem: string repetition
m="moon "
print(m*3)

s="stars "
print(s*4)

print("* "*3+s+"* "*3)

r="rocket"
print(r*5)

#4 fourth prblm : print half of string 
st="python"
l=len(st)
le=int(l/2)
first_half=st[:le]
sec_half=st[le:]


st="marolix technology"
le=len(st)
for i in range(le) :
    if st[i]==" ":
        num=i
first_half=st[:num]
sec_half=st[num:]
print(first_half)
print(sec_half)

st="training assignment"
first=""
sec=""
for i in st:
    first+=i
    if i==" ":
        break
print(first)

st="software coaching"
first=""
sec=""
for i in st:
    first+=i
    if i==" ":
        break

le=len(first)
second=st[le:]
print(first)
print(second)


st="dotnet"
l=len(st)
le=int(l/2)
print(st[:le])
print(st[le:])


#5 fifth prblm: pass or fail
score =int(input("enter marks : "))
if score<50:
    print("Sorry u have been failed in the examination")
elif score>=50 and score<80:
    print("U have been passed in the examination ")

else:
    print("Congrats u have scored distinction")


    #6 sixth problerm: verify if eligible to vote
age=int(input('enter age: '))
if age>=18:
    print("You are eligible to vote")
else:
    print("Sorry , u are not eligible")


#7 seventh prblm: square or not
a=int(input("enter firstone : "))
b=int(input("enter sec num : "))
if a==b:
    print("Hey its a square")
else:
    print("Its not a square")


#8 eigth prblm: even and odd seperations

n=10
even=[]
odd=[]
for i in range(n):
    if i==0 or i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,end=" ")
print(odd,end=" ")


n=20
even=[]
odd=[]
for i in range(1,n):
    if i%2==0:
        continue
    odd.append(i)
print(odd)

n=15
even=""
odd=""
for i in range(n):
    if i==0 or i%2==0:
        even+=str(i)+" "
    else:
        odd+=str(i)+" "

print(even)
print(odd)


#9 ninth prblm: print patterns

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


a=5
b=7
for i in range(a):
    print("* "*b)


n=5
for i in range(1,n+1):
    hollow="  "*(n-i)
    star="* "*i
    print(hollow+star)


n=5
for i in range(1,n+1):
    if i==1 or i==2 or i==n:
        hollow="  "*(n-i)
        star="* "*i
        print(hollow+star)
    else:
        hollow="  "*(n-i)
        gap="  "*(i-2)
        print(hollow+"* "+gap+"* ")
    print()


a=4
b=7
for i in range(1,a+1):
    if i==1 or i==a:
        print("* "*b)
    else:
        print("* "+"  "*(b-2)+"* ")

