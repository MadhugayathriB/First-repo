#1 count upper and lower cases in astring
def upper_and_lower(string):
    up=0
    low=0
    space=0
    spl=0
    for i in string:
        if i.isupper():
            up=up+1
        elif i.islower():
            low=low+1
        elif i.isspace():
            space=space+1
        else:
            spl=spl+1
    print("Upper alpahbets are "+str(up))
    print("lower alphabets are "+str(low))
    print("spaces are "+str(space))
    print("spl chaecaters are "+str(spl))

st=input("enter string : ")
upper_and_lower(st)

#2 create disctint elemnts list
def distinct(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    print(new)
s=input("enter list : ")
s=s.split()
distinct(s)

#3check is string is a pangram or not 
def pangram(s):
    new=""
    for i in s:
        if i==" ":
            pass
        elif i in new:
            pass
        else:
            new=new+i
    if len(new)==26:
        print("Its a pangram")
    else:
        print("Its not a pangram")

st=input("Enter string : ")
pangram(st)

#4print list with values having squares from (1-10)
def square(a,b):
    new=[]
    for i in range(a,b):
        sq=i**2
        new.append(sq)
    print(new)

a=int(input("enter first num : "))
b=int(input("enter sec num : "))
square(a,b)

#5 sum of all num in a list
def add(l):
    count=0
    for i in l:
        count=count+int(i)
    print(count)
s=input("entr : ")
s=s.split()
add(s)

#6 sum of values 
def sumof(*s):
    count=0
    for i in s:
        count=count+int(i)
    print(count)


sumof(1,2,3,4,5)