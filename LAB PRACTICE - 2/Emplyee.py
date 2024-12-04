class SalaryNotInRangeError(Exception):
    pass

class Emplyee :

    def __init__(self, name ,salary):
        self.name = name
        self.salary = salary
    def Display_Salary(self):
        
        if self.salary < 10000 and self.salary > 50000:
          raise SalaryNotInRangeError("Not Allowed")
        
        else :
            print (self.name ,self.salary)
    
try:
    emp = Emplyee("Ovi",30000)

    # print (emp)
    emp.Display_Salary()


    
except SalaryNotInRangeError :
    print ("Invalid Salary ")


