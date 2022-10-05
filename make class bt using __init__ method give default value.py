# write a python script to init default value for user object __init__ method.



class student:
    def __init__(self,name,age):
        self.nam=name 
        self.ag=age
    def show(self):
        print(self.nam)
        print(self.ag)


s1=student("gaurav",25)
s2=student("patel",26)
print(s1.show()) 
print(s2.show())       