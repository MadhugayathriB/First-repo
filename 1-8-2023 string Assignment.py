
#string slicing
st=input("enter string : ")
print(st[:9])

#reverse string
print(st[::-1])

#string slicing with diff
l=len(st)
print(st[:l:3])

#membership operators
st=input("enter string: ")
sub=input("Enter substring: ")
if sub in st:
    print("Yes its there")
else:
    print("Its not found")

sub="bus"
if sub in st:
    print("Its there")
else:
    print("NO its not there")

# comparing strings

print(ord("A"))#gives unicode value
print(chr(78))#gives character

print("Apple">"apple")
print("aloo65"<"aloo75")

#remove spaces
st=input("Enter string: ")
print(st.strip(st))

#find index in string
st=input("Enter string: ")
print(st.find("n"))# gives first "n"
print(st.rfind("n"))# gives lAST "n"
print(st.find("n",0,17))#gives n in between given start and end index
print(st.find("p"))#returns -1 if not found

#index()
st=input("Enter string : ")
print(st.index("n"))
print(st.rindex("n"))
print(st.index("p"))# returns error if not there


#counting
st=input("Enter string : ")
print(st.count("n"))

