#1 extend two lists
l=int(input("enter length: "))
one=[]
for i in range(l):
    char=int(input("value of index "+str(i)+": "))
    one.append(char)

l=int(input("enter length: "))
two=[]
for i in range(l):
    char=int(input("value of index "+str(i)+": "))
    two.append(char)
one.extend(two)
print(one)


#2print sum of the list

s=int(input("enter size of list: "))
add=[]
for i in range(s):
    val=int(input("value of index "+str(i)+": "))
    add.append(val)

print(sum(add))

#OR

# count=0
# for i in add:
#     count=count+i

# print(count)


#3 print even numbers in a list

l=int(input("enter length: "))
even=[]
for i in range(l):
    value=int(input("value of index "+str(i)+": "))
    if value%2==0:
        even.append(value)
    
print(even)

#4 print odd numbers in a list

s=int(input("enter size of list: "))
odd=[]
for i in range(s):
    val=int(input("value of index "+str(i)+": "))
    if val%2 != 0:
        odd.append(val)
print(odd)


#5 delte elemnt of given index from list

l=int(input("enter length: "))
ind=int(input("Index to be deleted : "))
fifthlist=[]
for i in range(l):
    char=int(input("value of index "+str(i)+": "))
    fifthlist.append(char)
for i in range(l):
    if i==ind:
        fifthlist.remove(fifthlist[i])
print(fifthlist)


#6 delete  any element from list
l=int(input("enter length: "))
value=int(input("character to be deleted : "))
sixthlist=[]
for i in range(l):
    char=int(input("value of index "+str(i)+": "))
    sixthlist.append(char)
for i in sixthlist:
    if i==char:
        sixthlist.remove(value)
print(sixthlist)

#7 insert elemnt at given location

s=int(input("Enter size of list : "))
ind=int(input("enter where to be inserted : "))
value=int(input("Enter what to be inserted : "))
insertlist=[]
for i in range(s):
    char=int(input("Enter value of "+str(i)+" : "))
    insertlist.append(char)
insertlist.insert(ind,value)
print(insertlist)


#8 insert elemnt at last

l=int(input("enter length: "))
value=(input("character to be inserted : "))
eighthlist=[]
for i in range(l):
    char=int(input("value of index "+str(i)+": "))
    eighthlist.append(char)
eighthlist.append(value)
print(eighthlist)


#9 check size of two lists
first=input("Enter list : ")
firstlist=first.split(",")
sec=input("Enter list : ")
seclist=sec.split(",")
if len(firstlist)==len(seclist):
    print("Both lists are of same size")
else:
    print("Both lists are not of same in size")
