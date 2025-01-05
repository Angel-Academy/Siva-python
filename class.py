
class bike:
    model="none"
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
        print(self.model)
b1 = bike("honda",2000,"red")
#b2 = bike("r15",2018,"black")
#b3 = bike("mt",2020,"yellow")
b1.model="tvs"
print(b1.model)
del b1
print (b1.model)
'''
class bike:
    model="none"
    def __init__(self):
        self.model=str(input("enter your model:"))
        self.year=int(input("enter your model year:"))
        self.color=str(input("enter your color:"))
    def print(self):
        print(f" model={self.model} \n year={self.year} \n color={self.color}")
b1=bike()
b2=bike()
b3=bike()
b1.print()
b2.print()
b3.print()
'''
