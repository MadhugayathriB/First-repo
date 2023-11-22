#jion strings
# s="I am fine"
# st=s.split()
# print(" ".join([s,"thankyou"]))



#replace all vowels 
# v="a,e,i,o,u"
# s=input("enter string: ")
# ans=""
# for i in s:
#     if i in v:
#         i=""
#     ans=ans+i
# print(ans)


#replcae first vowel
# v="a,e,i,o,u"
# s=input("enter string: ")
# for i in range(len(s)):
#     if s[i] in v:
#         s=s[:i]+""+s[i+1:]
#         break
# print(s)



#count frequency of string
# s=input("enter string: ")
# d={}
# for i in s:
#     if i not in d:
#         d[i]=s.count(i)
#     else:
#         d.update({i:s.count(i)})
# print(d)
#count hughest fre n lowest frequwncy
# s=input("enter string: ")
# d={}
# for i in s:
#     if i not in d:
#         d[i]=s.count(i)
#     else:
#         d.update({i:s.count(i)})
# ma=max(d.values())
# for i in d:
#     if d[i]==ma:
#         print(i)
# mi=min(d.values())
# for i in d:
#     if d[i]==mi:
#         print(i,end=" ")



#swapcase
# s=input("enter string: ")
# res=''
# for i in s:
#     if i.isupper():
#         res=res+i.lower()
#     else:
#         res=res+i.upper()
# print(res)
# print(s.swapcase())



#sort the string both ascending and descending
# s=input("enyer string:")
# res="".join(sorted(s))
# print(res)#ascending order
# print(res[::-1])#descending order




#LCM of two digits
# first=int(input("enter num: "))
# sec=int(input("enter num: "))
# if first>sec:
#     great=first

# else:
#     great=sec
# for i in range(great,(first*sec+1)):
#     if i%first==0 and i%sec==0:
#         print(i)
#         break



#hcf of two digits
# first=int(input("enter num: "))
# sec=int(input("enter num: "))
# if first>sec:
#     small=sec
# else:
#     small=first

# for i in range(1,small+1):
#     if first%i==0 and sec%i==0:
#         result=i
        
# print(result)
    


#split and jion string
# s=input("enter string: ")
# r=s.split("a")
# print(r)
# res="a".join(r)
# print(res)



#rotate string number of times-right
# s=input("enter string: ")
# n=int(input("num of rotations:"))
# if n<len(s):
#     r=n
# else:
#     r=n%len(s)
# start=s[:r]
# last=s[r:]
# print(last+start)

# #roatate left
# s=input("enter string: ")
# n=int(input("num of rotations:"))
# if n<len(s):
#     r=n
# else:
#     r=n%len(s)
# start=s[:len(s)-r]
# last=s[len(s)-r:]
# print(last+start)



#find 2 largest numbers in list
# l=[1,5,6,2,7,9,]
# res=sorted(l)
# first,sec=res[len(res)-1],res[len(res)-2]
# print("first highest num in arry: " ,first)
# print("second highest num in arry :" ,sec)



#remove particular cahracter from string
# s=input("Enter string: ")
# c=input("Enter char: ")
# res=s.replace(c,"")
# print(res)

#using index
# s=input("Enter string: ")
# i=int(input("Enter index: "))
# res=s.replace(s[i],"")
# print(res)






