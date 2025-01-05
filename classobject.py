class student:
    model="none"
    def __init__(self):
                 self.name=str(input("enter ur name:"))
                 self.roll=int(input("enter ur rollnumber:"))
                 self.age=int(input("enter ur age:"))
    def print(self):
        print(self.name)
s1=student()
s1.print()
 
