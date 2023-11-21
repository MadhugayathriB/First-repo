class Data: #details stored in company data
    def __init__(self):
        self.name="Isha"  #public variable
        self._salary=15000  #protected variable
        self.__hike_percent="10%"  #private variable
    def display(self):
        print(self.name ," salary is ",self._salary," percentage of hike to be given is ",self.__hike_percent)

class Employeeview(Data):# details viewed as per employee ,percentage of hike to be given should be hidden from employee.
    def dis(self):
        super().display()# can access pvt s attribiutes in form of methods bit not attributes directly.
    def result(self):
        print("Name of Employee: " ,self.name )
        print("Salary of Employee: ",self._salary )
        print("Hike percentage of Employee: ",self.__hike_percent )# cananot display hike percent to employee as its confidential.



# d=Data()
# print(d.name) #can acces directly using ref variable outside
# print(d._salary) #can access directly using ref variable outside
# print(d._Data__hike_percent) #can access using classaname outside using "_classanme" infornt of variable.
# d.display()

# print("        ")

#e=Employeeview()
# print(e.name)
# print(e._salary) #protected variables can b assesed even after inherited to child class
# e.result()
# print(e._Employeeview__hike_percent)# pvt varaibles cannot be accesed outside parent class or inherited.
#e.dis()



#pvt,protcted can be accesed using obj ref var in other class calling in methods but pvt attributes indivdually cannot be displyed in other class.
class Sales:
    def __init__(self):
        self._total_sales = 0  # Protected attribute to store total sales
        self.__sales_list = []  # Private attribute to store individual sales

    def add_sale(self, amount):
        if amount > 0:
            self.__sales_list.append(amount)
            self._total_sales += amount
        else:
            print("Invalid sale amount. Sale amount should be greater than 0.")

    def get_total_sales(self):
        return self._total_sales

    def get_sales_list(self):
        return self.__sales_list


class Finance:
    def __init__(self, sales_obj):
        self._sales = sales_obj
    def display(self):
        print(self._sales._total_sales) #can print becuase protected attribute.
        print(self._sales._Sales__sales_list)  #can print private attribute becuase classname is used after obj ref var. private attribute
        print(self._sales.__sales_list)  #cannot print becuase private attribute
        


    def calculate_profit(self, expenses):
        total_sales = self._sales.get_total_sales()#can disaply becuase methods can be called.
        profit = total_sales - expenses
        return profit


# Creating Sales object
sales_record = Sales()

# Adding individual sales
sales_record.add_sale(1000)
sales_record.add_sale(1500)
sales_record.add_sale(800)

# Creating Finance object using the Sales object
finance_analysis = Finance(sales_record)

# Calculating profit
expenses = 2500
profit = finance_analysis.calculate_profit(expenses)

print("Total Sales:", sales_record.get_total_sales())
print("Sales List:", sales_record.get_sales_list())
print(f"Profit after expenses of ${expenses}: ${profit}")
finance_analysis.display() #cannot print bcoz pvt aatribute


