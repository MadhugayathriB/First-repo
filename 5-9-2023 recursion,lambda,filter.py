#recusrion examples

#1 
def sum_nums(n):
    if n<=0:
        return 0
    else:
        return n+sum_nums(n-1)
num=int(input("Enter num: "))
res=sum_nums(num)
print(res)

#2
def stars(n):
    print(n*"* ")

    if n<=1:
        return 1*"* "
    else:
        stars(n-1)
num=int(input("Enter num: "))    
stars(num)
    

#3
def fibonacci(n):
    if n<=1:
        return n 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter num: "))
res=fibonacci(num)
print(res)

#lambda function examples

#1-if num is even
num=int(input("enter num: "))
res=lambda n: n%2==0
print(res(num))

#2-creating list using split
st=input("Enter input: ")
res=lambda s: s.split()
print(res(st))

#3-membership checking
st=input("Enter string: ")
s=input("Enter char:")
res=lambda st,s: s in st
print(res(st,s))



#filter function examples

#1-filter odd numbs
l=[1,2,3,4,5,6,7]
res=list(filter(lambda x:x%2!=0, l))
print(res)

#2-filter prime numbers
l=list(range(2,11))
def prime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count=count+1
    if count==1:
        return n
    else:
        return False
res=list(filter(prime,l))
print(res)

#3-filter if divisible by 5
l=list(range(1,101))
def divisible(n):
    if n%5==0:
        return True
    else:
        return False
    
res=list(filter(divisible,l))
print(res)





