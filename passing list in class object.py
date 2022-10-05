# WRT 7th question create 3 laptop object and add them to the list in the sorted order 
# on the ram size.   


class roll:
    def __init__(self,roll1,roll2):
        self.row1=roll1
        self.row2=roll2

list=[]
list.append(roll(1,2))
list.append(roll(3,4))
list.append(roll(5,6))
for i in list:
    print(sorted(i.row1 ,i.row2, sep = ' ')) 
               