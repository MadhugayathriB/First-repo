# str = "marolix technology"
# dict ={}
# for s in str:
#    dict[s]=s.count(s)
# print(dict)
# str="marolixtechnologyy"
# five={}
# for i in str:
#     if i in five:
#         pass
#     else:
#         five.update({i: str.count(i)})
# print(five)
# 
#To know prime numbers from 0-10
# n=10
# l=[]

# for i in range(2,n+1):
#     count=0
#     for j in range(2,n+1):
#         if i%j==0:
#             count=count+1
#     if count==1:
#         print(i," is a prime number")
#         #0r l.append(i)

# l=[1,4,8,3,8,3,0,3,75,8,3]
# # l.sort()
# print(sorted(l))
# def sumof(*se):
#     count=0
#     for i in se:
#         count=count+int(i)
#     print(count)

# s=input("enter list: ")
# s=s.split()
# se=tuple(s)
# sumof(1,2,3,4,5)
#s="nu76fbhyt @#%6%5fvb"
# spl=""
# for i in s:
#     if  i.isalpha():
#         spl=spl+i
# print(spl)

# def pangram(s):
#     old=""
#     new=""
    
#     s=s.lower()
#     for i in s:
#         if i.isalpha():
#             old=old+i
#     for i in old:
#         if i not in new:
#             new=new+i
#     if len(new)==26:
#         print("Its a pangram")
#     else:
#         print("Its not a pangram")

# st=input("Enter string : ")


# nums=list(range(2,11))

# res=filter(lambda x: all(x%i!=0 for i in range(2,x)),nums)
# print(list(res))

# l=list(range(5))
# def squares(n):
#     return n**2
# print(list(map(squares,l)))


# sq=lambda n: n**2
# print(list(map(sq,l)))
    
# def stars(n):
#     print(n*"* ")

#     if n<=1:
#         return 1*"* "
#     else:
#         stars(n-1)
# num=int(input("Enter num: "))    
# stars(num)


# def counting(q):
#     a=[]
#     n=[]
#     for i in q:
#         if i.isdigit():
#             n=n+[i]
#         else:
#             a=a+[i]
#     l=len(a)
#     res=""
#     for i in range(l):
#         alp=a[i]
#         num=int(n[i])
#         r=(alp*num)
#         res=res+r
#     print(res)
# q="a2b3c1d4"
# counting(q)

# def pattern_recursion(n):

#     if n > 0:
#         print("* " * n)
#         pattern_recursion(n - 1)

# pattern_recursion(5)

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     else:
#         return base*power(base,exponent-1)
# res=power(2,6)
# print(res)

# dict = {"country101": {"country":"india" , "capital":"delhi"} ,"country102":{"country":"pakistan","capital":"islamabad"},"country103":{"country":"china","capital":"beijing"},"country104":{"country":"usa","capital":"washington"},"country105":{"country":"france","capital":"paris"}}
# def signup(code,countryname,capitalname):
#      code=input("Enter countrycode: ")
#      countryname=input("Enter country: ")
#      capitalname=input("Enter capital: ")
#      dict[code]={"country":countryname,"capital":capitalname}
#      print(dict)
# def register(code,countryname,capitalname):
#      code=input("Enter country code : ")
#      if code in dict.keys():
          
#         countryname=input("Enter country: ")
     
#         if countryname==dict[code]["country"]:
#             capitalname=input("Enter capital: ")
#             if dict[code]["capital"]==capitalname:
#                print("You are correct")
#             else:
#                print("Your answer is wrong")

#      else:
#           print("Loading to signup page .....")
#           signup(code,countryname,capitalname)
#           print("country is Succesfully registered")
# register(101,"pakistan","islamabad")

# for i in range(2,10):   
#    for j in range(2,i):
        
#       if i%j==0:
#          break
#    else:
#       print(i)
    
from functools import *
import math 
from math import *
import random
from random import * 
# import string

# print(random())  #gives random num from 0-1
# print(randint(5,10))   #gives random num from 5-10 
#print(chr(randint(ord("a"),ord("z"))))# gives any random alphabet from a-z
# print(choice("abgtrecvhh"))# prints any alphabet in given sequense string or list.
#print(math.factorial(5))#prints factorial
# s="marolixtechnologysolutions"
# print(s.rfind("o",5,20))
# d={"madhu":"python","navya":"testing","anu":"python","praveen":"python","rushita":"devops"}
# for k,v in d.items():
#     if v=="python":
#         print(k)
#         
 # calculate the bill of order
# menu={"vegloaded":120,"farmfresh":180,"non_veg loaded":230,"spiceddoublechicken":250}
# additionals={"extra cheese":20,"extra ketchup":30}

# o=int(input("Numof items needed:"))



# bill=0
# for i in range(o):
#     a=input("enter pizza name:")
#     b=int(input("enter quantity:"))
#     if a in menu:
#         bi= menu[a]*b
#         bill+=bi
# c=input("enter a add on,type 1 else type 0:")

# if c=="1":
#     d=input("enter addon:")
#     if d in additionals:
#         bill=bill+additionals[d]
#         print(f'total prize:{bill}')
#     else:
#             print("add on not found")
# else:
#     print(f'total prize:{bill}')
# 

# def result():
#     employee_list={}
#     pythonlist=[]
#     javalist=[]
#     devopslist=[]
#     dotnetlist=[]
#     testinglist=[]
#     num_of_employees=int(input("Enter num of employees: "))
#     for i in range(num_of_employees):
#         domain=input("Enter domain: ")
#         name=input("Enter name: ")
#         emp_id=input("Enter emp_id: ")
#         email=input("Enter mail: ")
#         d=[name,emp_id,email]
#         if domain=="python":
#             pythonlist=pythonlist+[d]
#             employee_list["python"]=pythonlist
#         elif domain=="java":
#             javalist=javalist+[d]
#             employee_list["java"]=javalist
#         elif domain=="devops":
#             devopslist=devopslist+[d]
#             employee_list["devops"]=devopslist
#         elif domain=="dotnet":
#             dotnetlist=dotnetlist+[d]
#             employee_list["dotnet"]=dotnetlist
#         elif domain=="testing":
#             testinglist=testinglist+[d]
#             employee_list["testing"]=testinglist    
#     print(employee_list)#prints entire list
#     dom=input("Enter domain: ")
#     print(employee_list[dom])#prints only details of one domain
# result()


