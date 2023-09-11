
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
s="nu76fbhyt @#%6%5fvb"
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

# num=6
# for i in range(num):
#     print("* "*(num-i))


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
