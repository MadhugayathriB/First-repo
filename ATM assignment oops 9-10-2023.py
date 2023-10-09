class atm():
    amount=0
    pin=0
    @staticmethod
    def functions():
        Req=(input("Enter req: "))
        
        if Req=="1":
            atm.pingeneration()
        elif Req=="2":
            atm.deposit()
        elif Req=="3":
            atm.withdraw()
        elif Req=="4":
            atm.balanceenquiry()
        elif Req=="0"  :
            print("Thankyou visit again")
     
    @staticmethod
    def pingeneration():
        ENTERPIN=int(input("Enter num: "))
        atm.pin=ENTERPIN
        print("Your pin has been set")
        atm.functions()
    @staticmethod
    def deposit():
         a=int(input("Enter amount to be deposited: "))
         atm.amount=a+atm.amount


         print("your acc has ", atm.amount)
         atm.functions() 
    
    @staticmethod
    def withdraw():
        if atm.pin != 0:
        
            p=int(input("Enter pin: "))
            if p==atm.pin:

                atm.withdrawlamount=int(input("Enter amnt to be withdrawn: "))
                if atm.amount>=atm.withdrawlamount:
                   print(atm.withdrawlamount," has been withdrawn from your account.")
           
                   atm.balance=atm.amount-atm.withdrawlamount
                   atm.amount=atm.balance
                else:
                   print("Your account have insuffucient funds, please deposit.")
            else:
                print("Enter correct pin")
        else:
            print("Please set a pin for your atm.")
        atm.functions()
    @staticmethod
    def balanceenquiry():
        atm.balance=atm.amount
        print("Yor acc balance is ",atm.balance)
        atm.functions()
print("Enter 1 for pingeneration")
print("Enter 2 for deposit")
print("Enter 3 for withdrwal")
print("Enter 4 for balance enquiry")
c=atm()
c.functions()





