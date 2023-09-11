dict={"india":"delhi","usa":"washington","srilanka":"columbo","afghanistan":"kabul","maldives":"male","pakistan":"islamabad","china":"beijing","egypt":"cairo","france":"paris"}
def signup(country,capital):
     country=input("Enter country: ")
     capital=input("Enter capital: ")
     dict[country]=capital
     print(dict)
def register(country,capital):
     country=input("Enter country: ")
     
     if country in dict.keys():
          capital=input("Enter capital: ")
          if dict[country]==capital:
               print("You are correct")
          else:
               print("Your answer is wrong")

     else:
          print("Loading to signup page .....")
          signup(country,capital)
          print("country is Succesfully registered")
register("pakistan","islamabad")
