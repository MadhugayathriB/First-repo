#1 remove character from a string
st=input("Enter string : ")
ch=input(" Enter character : ")
method=st.replace(ch,"")
print(method)

#2 check if string is palinmdrome or not
st1=input("Enter st : ")
st2=st1[::-1]
if st1==st2:
    print("Its a palindrome")
else:
    print("Its not a plaindrome")


#3 check character is vowel or consonant

character=input(" Enter character : ")
vowels="a,e,i,o,u,A,E,I,O,U"
if character in vowels:
    print("Its an vowel.")
else:
    print("Its a consonant")

#4 replace string space with character 
st="Marolix Technologies has been found in 2011."
cha=" "
result=st.replace(cha,"-")
print(result)

#5 count alpahabets digis and spl characters
st=input("Enter password: ")
alpha=0
digits="0,1,2,3,4,5,6,7,9,8"
digit=0
spl=0
for i in st:

    if i in digits:
        digit=digit+1
    elif i.isupper() or i.islower():
        alpha=alpha+1
    else:
        spl=spl+1
print("alpha : " +str(alpha))
print("digit : "+str(digit ))
print("spl : "+ str(spl))

#6 remove all balnk spcaes in string 
st=input("Enter string : ")
result=st.replace(" ","")
print(result)



#7 sum of integers in string
st=input("Enter string : ")
li=[]
for i in st:
    if i.isdigit():
        li=li+[int(i)]
print(sum(li))

#8remove repeated character from string
st=input("Enter strimg : ")
li=[]
set=set()
for i in st:
    if st.count(i)==1:
        li=li+[i]
    else:
        set.add(i)# removes repaeted alphabets

result=li+list(set)
print(result)


#9 count occurance of characters in string
st=input(" Enter string : ")
li=[]

for i in st:
    li=li+[i]
set_1=set(li)

for i in set_1:
    print(i+" : "+ st.count(i))

    



#10 find anagrams or not - having same alphabets
st1=input("Enter string : ")
st2=input("Enter string : ")
li=[]
for i in st2:
    li=li+[i]

count=0

if len(st1)==len(st2):
    for i in st1:
        if i in li:
            if st1.count(i)==st2.count(i):
                count=count+1
                
        else:
            pass


if count==len(st1):
    print("Its an anagram")
else:
    print("Its not an anagram")

#11 sort alhbaets and nect digits in string
st=input("Enter string : ")
alpha=[]
num=[]
for i in st:
    if i.isdigit():
        num=num+[i]
    else:
        alpha=alpha+[i]
result=alpha+num

final="".join(result)
print(final)


    