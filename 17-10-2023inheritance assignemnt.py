#Types of inheritance

#single inheritance
class laptop():
    def m1(self):
        print("I am laptop.")
class hp(laptop):
    def m2(self):
        print("I am hp laptop.")
h=hp()
h.m1()
h.m2()

#hierarchial inheritance
class cashkaro():
    def m1(self):
        print("Hurray its cashback bonanza...")
class amazon(cashkaro):
    def m2(self):
        print("You will get 5% cashback.")
class myntra(cashkaro):
    def m3(self):
        print("You will get 7%cashback.")
a=amazon()
a.m1()
a.m2()
m=myntra()
m.m1()
m.m2()

#multiple inheritance
class water():
    def m1(self):
        print("I am water")
class teapowder():
    def m2(self):
        print("I am teapowder")
class decoction(water,teapowder):
    def m3(self):
        print("I am decoction ...")
d=decoction()
d.m1()
d.m2()
d.m3()

#multilevel inheritance
class milk():
    def m1(self):
        print("I am milk")
class curd(milk):
    def m2(self):
        print("I am curd make from milk")

class buttermilk(curd):
    def m3(self):
        print("I am buttermilk made from curd")
b=buttermilk()
b.m1()
b.m2()
b.m3()

#hybrid inheritance
class rice():
    def m1(self):
        print("I am rice")
class uraddal():
    def m2(self):
        print("I am uraddal")
class dosabatter(rice,uraddal):
    def m3(self):
        print("I can make tasty dosa...")

class ragidosa(dosabatter):
    def m4(self):
        print("Ragidosa is helathy susbstitute.")
class greengramdosa(dosabatter):
    def m5(self):
        print("I am greegram dosa")

class onionpesarattu(greengramdosa):
    def m6(self):
        print("ENjoy onion pesarattu.")
d=dosabatter()
d.m1()
d.m2()
d.m3()
g=greengramdosa()
g.m3()
o=onionpesarattu()
o.m6()
