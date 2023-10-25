class hospital:
    def __init__(self):
        self.data={}
        print("Welcome to our hospital ,Please select the option")
        self.options()
    def options(self):
        print("select 1 to enroll\nselect 2 for overallpatientsview\nselct 3 to search patient data\nselect 4 to delete patient data\nslect 5 to update patient data")
        option=int(input("Enter your option: "))
        if option==1:
            self.enroll()
        elif option==2:
            self.overallpatientsview()
        elif option==3:
            self.search()
        elif option==4:
            self.delete()
        elif option==5:
            self.update()
        else :
            print("Thankyou...")
    def enroll(self):
        id=int(input("Enter ID: "))
        if id in self.data:
            print("This ID.no has already been taken.")
        else:
            name=input("Enter patient name: ")
            age=(input("Enter age: "))
            Temp=(input("Enter temperature: "))
            illness=input("Enter the health issue: ")
            res={"name":name,"age":age,"Temp":Temp,"illness":illness}
            self.data[id]=res
            print("patient with, ",id ," number has been enrolled succesfully.")
        self.options()
    def overallpatientsview(self):
        if self.data=={}:
            print("No patients are enrolled yet.")
        else:
            l=len(self.data)
            print("There are ",l," patients in the hospital.")
            print(self.data)

        self.options()
    def search(self):
        id=int(input("Enter required ID: "))
        if id in self.data:
            print(self.data[id])
        else:
            print("Given ID is not yet enrolled in the hospital")
        self.options()
    def delete(self):
        id=int(input("Enter required ID: "))
        if id in self.data:
            del self.data[id]
            print("Patient data with ID.no",id ," number has been deleted succesfully.")
        else:
            print("Given ID is not yet enrolled in the hospital")
        self.options()
    def update(self):
        id=int(input("Enter required ID: "))
        if id in self.data:
            print("choice: ",["name","age","Temp","illness"])
            choice=input("Enter choice: ")
            updatedvalue=input("Enter value: ")
            res=self.data[id]
            res[choice]=updatedvalue
            print("Patient data with ID.NO ",id ," number has been updated succesfully.")
        else:
            print("Given ID is not yet enrolled in the hospital")
        self.options()
result=hospital()