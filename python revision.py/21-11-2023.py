#reverse the number
# num=int(input("Enter num: "))
# old=num
# r=0
# while num !=0:
#     n=num%10
#     r=r*10+n
#     num=num//10
# if old==r:
#     print("ITS A PALINDROME")
# else:
#     print("NOT A PALINDROME")


#using recursion
# def palindrome(num):
#     if num<10:
#         return num
#     else:
#         return int(str(num%10)+str(palindrome(num//10)))
# num=int(input("Enter num: "))
# result=palindrome(num)
# if num==result:
#     print("ITS PALINDROME")
# else:
#    print("NOT A PALINDROME")



#swapping two numbers
# x=int(input("ENTER FIRST NUM: "))
# y=int(input("ENTER SEC NUM: "))
# x,y=y,x
# print("firstnum:",y)
# print("secnum: ",x )



#perfect number
# num=int(input("ENTER NUM: "))
# total=0
# for i in range(1,num):
#     if num%i==0:
#         total=total+i
# if num==total:
#     print("Its a perfect num")
# else:
#     print("Its not a perfect num")




#sum withoyt arithmetic operator
# l=[]
# for i in range(2):
#     one=int(input("ENTER NUM: "))
#     l.append(one)
# print(sum(l))



#find missing num in range of numbers(1-10)
# l=list(range(1,11))
# l2=[1,3,6,5,8,9,10]
# missing=set(l)-set(l2)
# print(list(missing))
 


#find avg of numbers
# l=[]
# for i in range(5):
#     one=int(input("ENTER NUM: "))
#     l.append(one)
# avg=sum(l)/len(l)
# print(avg)



#fibonacci by looping
# num=int(input("ENTER NUM: "))
# one=0
# two=1
# for i in range(0,num):
#     if i<=1:
#         result=i
#     else:
#         result=one+two
#         one=two
#         two=result
#     print(result)



#print prime num in range(0-10)
# for i in range(2,10):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#factorial withput recursion
# n=int(input("ENTER NUM: "))
# res=1
# for i in range(1,n+1):
#     res=res*i
# print(res)

# #using recusrion
# def factorial(num):
#     if num<=1:
#         return num
#     else:
#         return num*factorial(num-1)
# num=int(input("ENTER NUM: "))
# print(factorial(num))







