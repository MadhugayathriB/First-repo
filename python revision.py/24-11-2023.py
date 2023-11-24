#fibonacci using whileloop
# n=int(input("Enter range: "))
# i=0
# first=0
# sec=1
# while (i<n):
#     if i<=1:
#         result=i
#     else:
#         result=first+sec
#         first=sec
#         sec=result
#     print(result)
#     i=i+1


#using forloop
n=int(input("Enter range: "))
i=0
first=0
sec=1
for i in range(0,n+1):
    if i<=1:
        result=i
    else:
        result=first+sec
        first=sec
        sec=result
    print(result)
    i=i+1

