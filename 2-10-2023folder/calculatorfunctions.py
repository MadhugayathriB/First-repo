def add(*var):
    sum=0
    for i in var:
        sum=sum+int(i)
    print(sum)
    return
def sub(*var):
    sub=0
    for i in var:
        sub=int(i)-sub
    print(sub)
    return
def mul(*var):
    mul=1
    for i in var:
        mul=mul*int(i)
    print(mul)
    return
def div(*var):
    div=1
    for i in var:
        div=int(i)/div
    print(div)
    return