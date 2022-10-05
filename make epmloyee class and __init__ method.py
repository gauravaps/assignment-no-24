#define a class employee with instance object variables empid,name,salary.write __init__() method
#in the class to initialize instance object variables also define instance method to input
#field and display field values.
class employee:
    company="wipro"

    def __init__(self,empid,name,salary):
        self.emp=empid
        self.nam=name
        self.sal=salary
    def view(self):
        print("employee id is =" ,self.emp)
        print("name of employee =",  self.nam)
        print("salary of employee =", self.sal)
    @classmethod
    def show(self): 
        return self.company

s1=employee(101,"gaurav",5000)
print(s1.view()) 
print(employee.show())          



