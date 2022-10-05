# write a python script to create laptop class with 4 atrributes (brand ,ram,cpu ,hdd )
# and 2 method (showconfig() to print the values __init__() to initialize the values)

class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.bran=brand
        self.rm=ram
        self.cp=cpu
        self.hd=hdd
    def show(self):
        print("brand of the computer",self.bran) 
        print("ram of the compure is =" ,self.rm)
    def show1(self):   
        print("cpu of the computer is =" ,self.cp) 
        print("hdd of the computer is =" ,self.hd) 

s1=laptop("dell",8,"intel",1000) 
print(s1.show()) 
print(s1.show1())        
       
 
