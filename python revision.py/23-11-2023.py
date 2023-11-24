#contigous array
# l=[-2,5,-1,4,7,1,-4]
# sumarray=[]
# sublist=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)+1):
#         start=i
#         end=j
#         arr=l[start:end]
#         print(arr)
#         sublist.append(arr)
#         sumarray.append(sum(arr))
# m=max(sumarray)
# i=sumarray.index(m)
# print(sublist[i])


#all prime numbesr using lambda
# nums=list(range(2,11))
# res=filter(lambda x:all(x%i!=0 for i in range(2,x)),nums)
# print(list(res))



#list comprehension
# res=[x for x in range(11) if x%2==0]
# print(res)



#lambda
# res=lambda x:x**2
# print(res(5))



#tuple unpacking
# countries=("india","usa","china","uk")
# (delhi,washinton,beijing,london)=countries
# print(delhi)
# print(london)



#positionalarguments
# def fun(a,b):
#     print(a-b)
# fun(400,500)



# #keyword  arguments
# def fun(a,b):
#     print(a-b)
# fun(b=400,a=500)



#various length arguemnts
# def func(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# func(1,2,3,4,5)



#keyword various length arguemnts
# def func(**n):
#     for k,v in n.items():
#         print(k," - ",v)
# func(india="delhi",uk="london",china="beijing")



#form a matrix
# l=5
# b=5
# count=0
# for i in range(l):
#     list=[]
#     for j in range(b):
#         count=count+1
#         list.append(str(count))
#     print(" ".join(list))



#overlapping in string
# s1=input("Enyer string: ")
# s2=input("Enyer string: ")
# count=0
# for i in range(1,len(s1)):
#     first=s1[-i:]
#     sec=s2[:i]
#     if first==sec:
#         print(first)
#         count=count+1
# if count==0:
#     print("No Overlapping")




#seperate alphbets and numbers
# s="byt6tr5e4e45r78y8h"
# a=""
# n=""
# for i in s:
#     if i.isdigit():
#         n=n+str(i)
#     else:
#         a=a+str(i)
# print(a)
# print(n)



#ordered matrix
# l=3
# b=3
# list=[]
# for i in range(l):
#     np=input("Enter input: ")
#     res=map(int,np.split())
#     print(np)
#     for i in np:
#         i=int(i)
#         list=list+[i]
# so=sorted(list)
# x=0
# for i in range(l):
#     li=[]
#     for j in range(b):
#         li.append(str(so[x]))
#         x=x+1
#     print(" ".join(li))



#changing static and instance variable values
# class oops:
#     company="tcs"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("I am ",self.name," working at ",oops.company)

# ob=oops("madhu",23)
# ob.display()
# ob.name="abhinaya"
# ob.age=19
# oops.company="shell"
# ob.display()



#creating static and class methods
# class oops:
#     @classmethod
#     def cl(cls):
#         cls.name="madhu"
#         oops.age=23
#     @staticmethod
#     def st():
#         oops.company="walmart"
#     @classmethod
#     def display(cls):
#         print("I am ",oops.name," working at ",oops.company)
# ob=oops()
# ob.cl()
# ob.st()
# ob.display()
# oops.company="amazon"
# oops.name="abhinaya"
# oops.salary=50000
# ob.display()
# print(oops.salary)
# del oops.age


#inheritance
class par():
    def __init__(self):
        self.name="madhu"
    def cal(self):
        print("I am ",self.name)
    @classmethod
    def parclass(cls):
        print("I m parent classmethod")
class child(par):
    def display(self):
       print(self.name)
    @classmethod     
    def classme(cls):#accesing instance n constructor in class method
          super().parclass()#class n static methods can b accesed directly
          super(child,cls).__init__(cls)
          super(child,cls).cal(cls)
    @staticmethod
    def childsta():#only cls n static methods can b accesed
        super(child,child).parclass()
ob=child()
ob.display()
ob.classme()
ob.childsta()





    







