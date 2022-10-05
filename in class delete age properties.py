# write a python script to delete the age properties of the user.


from ast import Delete


class student:
    def f1(self,name,age):
        self.nam=name
        self.ag=age
        del self.ag
        return self.nam,self.ag
        
s1=student()
#del s1.ag
print(s1.f1("gaurav",25)) 
print(s1.f1("gaurav",25))
 
