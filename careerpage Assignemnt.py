

        
class admin():
      joblist={}
      def __init__(self,totalapplications):
            self.pwd=1234  
            self.totalapplications=totalapplications    
            self.password=int(input("Enter admin password: "))
            

            if self.password==self.pwd:
               print("Admin has been succesfully logged in ....")
               print("    ")
               self.options()
            else:
               print("Your password is wrong.")

      def options(self):
         print("press 1 to update jobs\npress 2 to read applications\npress 3 to logout")
         print("     ")
         option=int(input("Admin can select option: "))
         if option==1:
             self.update()
         elif option== 2:
             
             self.read()
            
         elif option==3:
             print("Admin Succesfully logged out...")
             print("    ")
        
        
      def update(self):
        jobtitle=input("Enter jobtitle: ")
        requiredpositions=int(input("Enter req.positions:"))
        qualification=input("Enter qualification required: ")
        post={"requiredpositions":requiredpositions,"qualification":qualification}

        admin.joblist.update({jobtitle:post})
        self.options()
      def read(self):
         l=len(self.totalapplications)
         print(f'{l} number of applications are received.')
         if self.totalapplications==[]:
             print("No applications are received yet...")
         else:
             print(self.totalapplications)
         self.options()

        

      def updatepassword(self):
                updatedpwd=int(input("Enter new pwd: "))
                self.pwd=updatedpwd
                self.options()

class user(admin):
                   def __init__(self):
                      self.applications=[]
            
                   def options(self):
            
                     if (super().joblist)=={}:
                      print("No jobs to apply")
                      print("user Logged out succesfully...")
                 
                     else:
                       print(super().joblist)
                       print("click 1 to apply\n click 2 to logout")
                       print("         ")
                       option=int(input("User can enter option: "))
                       if option==1:
                          self.apply()
                       elif option==2:
                          self.logout()
                
                   def apply(self):
                    self.name=input("Enter name: ")
                    self.age=int(input("Enter age: "))
                    self.qualification=input("Enter qualification: ")
                    self.mail=input("Enter mail: ")
                    self.linkedinurl=input("Enter url: ")
                    self.requiredjobtitle=input("Enter required position: ")
                    if self.requiredjobtitle in super().joblist:
                        
                        application={"name":self.name,"age":self.age,"qualification":self.qualification,"mail":self.mail,"linkedinurl":self.linkedinurl,"requiredjobtitle":self.requiredjobtitle}
                        self.applications.append(application)
                        print(f'Dear {self.name} your application has been received succesfully.')
                        print("      ")
                    else:
                        print("Jobrole you are looking is not vacate.")
                   
                   
                    self.options()
    
                   def logout(self):
                      print("user logged out succesfully")
                      print("    ")          


class careerpage(user,admin):
    def __init__(self):
        print("Welcome to careerpage...")
        print("    ")
        print("To login as user enter : user \nTo login as admin enter : admin")
        option=input("Enter login option: ")
        if option=="user":
            
             u.options()
             careerpage()
        elif option=="admin":
            app=u.applications
            admin(app)
            careerpage()
        else:
            print("Have a nice day ahead...")
u=user()      
c=careerpage()     









