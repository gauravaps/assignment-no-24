#write a python program to create a school class and 3 instance  variable and 1 class variable.
class school:
    schl="rewa"
     
    def f1(self,name):
        self.nam=name
        return self.nam
     
    def f2(self,age):
        self.ag=age
        return self.ag
    def f3(self):
        
        return self.schl   

    '''@classmethod    
    def get(cls):
        return cls.schl'''
    
s1=school()
print(s1.f1("gaurav")) 
print(s1.f2(25))
print(s1.f3())
print(s1.nam) 
#print(school.get())

                







