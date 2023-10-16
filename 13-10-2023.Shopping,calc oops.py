#shopping cart 
class shopping():
    def __init__(self):
        self.cart={}
        shopping.opinion(self)
    def opinion(self):
        print("press 1 to additem")
        print("press 2 to removeitem")
        print("press 3 to display cart")
        opinion=int(input("Enter your required choice: "))
        if opinion==1:
            self.additem()
        elif opinion==2:
            self.removeitem()    
        elif opinion==3:
            self.display()
        elif opinion==0:
            print("Happy shopping")
    def additem(self):
        item=input("Item needed: ")
        quantity=int(input("Enter quantity needed: "))
        price=int(input("Enter price: "))
        bill=price*quantity
        val={"quantity":quantity,"price":price,"bill":bill}
    
        if item in self.cart:
            s=self.cart[item]
            s["quantity"]=s["quantity"]+quantity
            s["bill"]=s["bill"]+bill
        else:
            self.cart[item]=val
        self.opinion()
    def removeitem(self):
        item=input("Enter itm to be removed: ")
        quantity=int(input("Enter quantity  to be removed: "))
        if item in self.cart:
            r=self.cart[item]

            r["quantity"]=r["quantity"]-quantity
            r["bill"]=r["bill"]-r["price"]*quantity
            if r["quantity"]==0:
                del self.cart[item]
        else:
            print(item, "is not added to cart")
        
        self.opinion()
    def display(self):
        self.cartvalue=0
        self.cartitems=0
        if self.cart=={}:
            print("Your cart is empty.")
        else:
            print(self.cart)
        
        for k,v in self.cart.items():
            
            self.cartvalue=self.cartvalue+v["bill"]
            self.cartitems=self.cartitems+v["quantity"]
            print(k," : ","quantity - ", v["quantity"],", bill", v["bill"])

        print("Your cart has ",self.cartitems," items in it.")
        print("Your cartbill is ",self.cartvalue)
        self.opinion()

s=shopping()
                
#calculator
class calculator:
    def __init__(self):
        self.functions()
    def functions(self):
        print("press 1 to add")
        print("press 2 to subtract")
        print('press 3 to multiply')
        print("press 4 for division")
        req=int(input("Enter req calc: "))
        if req==1:
            calculator.add(self)
        elif req==2:
            calculator.substract(self)
        elif req==3:
            calculator.multiply(self) 
        elif req==4:
            calculator.divide(self)       
    def add(self):
        first=int(input("Enter num: "))
        second=int(input("Enter num: "))
        print(first+second)
    def substract(self):
        first=int(input("Enter num: "))
        second=int(input("Enter num: "))
        print(first-second)
    def multiply(self):
        first=int(input("Enter num: "))
        second=int(input("Enter num: "))
        print(first*second)
    def divide(self):
        first=int(input("Enter num: "))
        second=int(input("Enter num: "))
        print(first/second)
                                                              
c=calculator()
