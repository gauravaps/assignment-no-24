# write a python script to create two object of the user class and asssign different values.

class student:
    
    def f1(self,name):
        self.nam=name
        return self.nam

s1=student()
s2=student()
print(s1.f1("gaurav"))  
print(s2.f1("patel"))     