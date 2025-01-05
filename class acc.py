import os
import webbrowser as web
import random as rd
import re
class acc:
    bank=None
    def __init__(self):
        self.name="sai"
        self.acc_no=12345678
        self.balance=100000000000
        self.phone_no=987654321
        self.pin=1234

        while(True):
            print("*****BANK ACCOUNT*****")
            print("1=create account")
            print("2=display accout")
            print("3=reset pin")
            print("4=withdraw amount")
            print("5=deposit amount")
            print("6=exit")
            select=int(input("press folllowing numbers to perform action: "))

            if select==1:
                self.create()
            elif select==2:
                self.display()
            elif select==3:
                self.reset()
            elif select==4:
                self.withdraw()
            elif select==5:
                self.deposit()
            elif select==6:
                print("successfully logout")
                break
            else:
                print("selected number is not found")

    def create(self):
        print("<<<<<<< enter your details >>>>>>> ")
        self.name=str(input("enter your name:")).lower()
        self.acc_no=int(input("enter your 12 digit acc number:"))
        self.balance=float(input("enter your balance amount:"))
        self.temp_ph=input("enter your 10 digit moblie number:")
        self.ph=re.fullmatch('[6-9][0-9]{9}',self.temp_ph)
        while self.ph==False:
            print("invalid phone number")
            self.temp_ph=input("enter your 10 digit moblie number:")
        else:
            self.phone_no==int(self.temp_ph)
        self.pin=int(input("enter your 4 digit pin:"))
        print("successfully create your account")
    def display(self):
        print("#####displaying ur account details#####")
        print(f" name:{self.name.title()}\n account number:{self.acc_no}\n balance:{self.balance} \n phone number:{self.phone_no}\n your account pin:{self.pin}")
    def reset(self):
        print("=======reset your pin=======")
        old_pin=int(input("enter your 4 digit old pin:"))
        if old_pin==self.pin:
            self.pin=int(input("enetr 4 didgit new number:"))
            print("successfully reset")
    def withdraw(self):
        print("/////////withdraw\\\\\\\\")
        enter_acc_no=int(input("enter bank account number:"))
        if enter_acc_no==self.acc_no:
            print(f"{self.name}")
            enter_pin=int(input("enter ur pin"))
            if enter_pin==self.pin:
                print("#enter the amount")
                withdraw_amount=int(input("enter the amount of withdraw:"))
                enter_ph=int(input("enter ur phone number:"))
                if self.phone_no==enter_ph:
                    otp = rd.randint(2000 , 9999)
                    f=open("otp.html","w")
                    f.write(f''' <html>
<head>
<title>withdraw</title>
</head>
<body>
<h1 style="color:red;"> <center> otp </h1>
<p style="color:blue;"> {otp} </p>
</body>
</html>''')
                    web.open("otp.html")
                    f.close()
                    enter_otp=int(input("enter ur otp:"))
                    if enter_otp==otp:
                        if withdraw_amount<=self.balance:
                            self.balance=self.balance-withdraw_amount
                            print(f"balance amount {self.balance}")
                        else :
                            print("insufficent balance")
                    else:
                        print("wrong otp")
                else:
                    print("wrong number")
            else:
                print("incorrect pin")
            
            
            
        else:
            print("invalid account number")
    def deposit(self):
        print("--------deposit-------")
        enter_acc_no=int(input("enter bank account number:"))
        if enter_acc_no==self.acc_no:
            print(f"{self.name}")
            enter_pin=int(input("enter ur pin:"))
            if enter_pin==self.pin:
                print("#enter the amount")
            else:
                print("incorrect pin")
            deposit_amount=int(input("enter the amount of deposit"))
            self.balance=self.balance+deposit_amount
            print(f"balance amount {self.balance}")
        else:
            print("invalid account number")   
c1=acc()


