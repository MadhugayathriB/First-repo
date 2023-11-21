#instance var (anythimg decalred using self or obj ref var)
# class employee():
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#         # can del any varaibles using Ex: del self.id 
#     def display(self):
#         self.salary=20000

# o=employee("madhu",23,9876)
# print(o.__dict__)#gives 3 variables
# o.display()# as salary is in display ,salary can b printed only after v call display
# print(o.salary)
# o.domain="python"# Can decalre using obj ref variable, domain is added to object
# print(o.__dict__)#gives 5 includes salary n dpmain
# del o.id#deltes id
# print(o.__dict__)#gives 4

#static variables:(decalred using classname or cls in class or using classname outside class in object)
class Employee():
    company="marolix"
    def __init__(self,name):
        self.name=name
        Employee.id=897
        print(Employee.company)
        self.age=15
        print(self.age)
        print(self.id)#can print using self or classnme
        
    def m1(self):
        self.age=23
        Employee.mail="madhy@gmail.com"
        
        print(Employee.mail)#To print or declare neded to write classnme or self
        print(self.age)
        print(self.mail)
        

    @classmethod
    def m2(cls):
        Employee.gender="female"
        cls.salary=25000
        Employee.company="tcs"
        print(Employee.company)#To print needed to write cls or clssanme
        print(cls.salary)
        print(cls.id)
        #cannot print name,age becuse name is decalred using self which are imstanmce variables

    @staticmethod
    def m3():
        Employee.domain="python"
        del Employee.mail #del employee mail
        print(Employee.domain)#to print needed to write clsanme
# e1=Employee("madhu")
# print(e1.__dict__)#gives only name b ecUSE only name in init method
# print(Employee.__dict__)
# # e1.m2()
# e1.m1()
# # Employee.id=1754# can modify id outside also using classname
# # print(e1.id)
# # del Employee.salary # deltes salary in the class 
# # print(e1.__dict__)#gives both name n age because both are decalred using self.
# e1.m3()
# # Employee.city="hyderabad"  #Can decalre var using classname only for static var 
# # print(e1.city)
# e2=Employee("anu")
# print(e2.city)
# print(e2.id)
# print(e2.company):


class parent:
    def __init__(self):
        print("I am constrcutor")
    def m1(self):
        print("I am intsnce method")
    @classmethod
    def m2(cls):
        print("I am class method")
    @staticmethod
    def m3():
        print("I am ststic method")
class child(parent):
    def __init__(self):
        print("I am child contsructor")
    def m4(self):#calling methods n cnstructor using super in intsnce method
        super().__init__()  
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m5(cls):
        super().m2()#using cls method cls n ststic methods are called directly
        super().m3()
        super(child,cls).__init__(cls)#constructor n intsnce methods should be written this way, childclassname, cls should b passed into argument.
        super(child,cls).m1(cls)

    @staticmethod
    def m6():#only ststic n cls methpds can be called from prent class using super
        super(child,child).m2()# childclass name should be passed twice.
        super(child,child).m3()
# c=child()
# c.m5()
#operator overloading
class marks():
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return(self.x+other.x)
# s1=marks(10)
# s2=marks(20)
# print(s1+s2)
class marks():
    def __init__(self,x):
        self.x=x
    def __sub__(self,other):
        return(self.x-other.x)
# s1=marks(30)
# s3=marks(10)
# print(s1-s3)#for sub mention sub n give "-".
#for multiplcation give __mul__ and "*".

# try:
#     print("try")# only if both staments are correct except wont print,even if only one is printed except is also printed.
#     print(10/0)
# except:
#     print("except")


class parent:
    def __init__(self):
        self.a=10
class child(parent):
    def __init__(self):
        print("I am child")
    def method(self):
        print(self.a)
c=child()
c.method()