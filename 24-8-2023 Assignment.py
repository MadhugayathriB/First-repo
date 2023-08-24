#1 .Add key to dictionaryd

one={}
for i in range(3):
    key=input("enter keys:")
    value=input("enter values:")
    one[key]=value

k=input("enter key: ")
v=input("enter value: ")
add={k:v}
one.update(add)
print(one)


#2 .check is dict already has a key
two={}
for i in range(3):
    key=input("enter keys: ")
    value=input("enter values: ")
    two[key]=value
k=input("Enter key :")

if k in two:
    print("Key alreday exits")
else:
    print("Key doesnt exist.")

#3 write program to iterate over dictionaries.
three={}
for i in range(3):
    key=input("enter keys: ")
    value=input("enter values: ")
    three[key]=value

for i in three.items():
    print(i)

#4 create dictionaries using keys from (1-15) and values are squares.
four=dict()

for i in range(1,16):
    n=(i)
    s=i**2
    four.update({n: s})
print(four)

#5 count occurances of string and fill it in dictionary
s=input("enter string : ")
five=dict()
for i in s:
    if i in five:
        pass
    else:
        five.update({i: s.count(i)})
print(five)

#6 sum all items in dictionary
six={}
for i in range(3):
    key=input("enter name: ")
    value=int(input("enter age: "))
    six[key]=value
sum_of_age=0
for i in six.values():
    sum_of_age=sum_of_age+i

print(sum_of_age)
#OR
print(sum(six.values()))



#7 combine values of 2  dictinaries if keys are common
d1={}
for i in range(3):
    key=input("enter key:")
    value=input("enter value: ")
    d1[key]=value
d2={}
for k in range(0,5):
    key=input("enter key: ")
    value=input("enter value:")
    d2[key]=value
for x,y in d2.items():
    if x in d1:
        d1[x]=d1[x]+d2[x]
    else:
        d1.update({x:y})


print(d1)


# #8 access dictionary key elemnet by indexing
eight={}
for k in range(3):
    key=input("enter keys")
    value=input("enter values")
    eight[key]=value
print(eight)




li=list(eight)
for i in range(len(li)):
    print(li[i])

    

#9 remove key from dictionary
nine={}
for k in range(3):
    key=input("enter keys")
    value=input("enter values")
    nine[key]=value
item=input("Enter item to be removed: ")
del nine[item]
print(nine)

#10 merge two python dictionaries
d1={}
for k in range(3):
    key=input("enter keys: ")
    value=input("enter values: ")
    d1[key]=value
d2={}
for k in range(3):
    key=input("enter keys: ")
    value=input("enter values: ")
    d2[key]=value
d1.update(d2)
print(d1)


