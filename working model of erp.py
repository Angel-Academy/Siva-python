#main program
ERP={"1226":{
     "name":"siva",
        "phone number":1234567890,
        "dob":"12345678",
        "password":"siva123",
        "roll number":"1226"
    
    }
    }
def userdefine(name,phone_no,dob,password,roll_no):
    ERP[roll_no]={
        "name":name,
        "phone number":phone_no,
        "dob":dob,
        "password":password,
        "roll number":roll_no
        }
    print("successfully create your acc")
def login(roll_no,password):
    if roll_no in ERP.keys():
       if ERP[roll_no]["roll number"]==roll_no and ERP[roll_no]["password"]==password:
           print("succussfully login into your acc")
       else:
           printt("unsuccessfull to login")
    else:
        print("acc not found")

def uprate(roll_no,name,phone_no,dob,password):
    if roll_no in ERP.keys():
        if name:
            ERP[roll_no]["name"]=name
        if password:
            ERP[roll_no]["password"]=password
        if phone_no:
            ERP[roll_no]["phone number"]=int(phone_no)
        if dob:
            ERP[roll_no]["dob"]=dob
        print("succcussfully uprated")
        print(ERP[roll_no])
    else :
        print("invaild acc")
        
   
while (True):
    print("ERP")
    print("1=create new acc")
    print("2=login into existing acc")
    print("3=uprate details")
    print("4=display acc")
    print("5=delete acc")
    print("6=logout")
    select=int(input("enter any one number from 1 to 6:"))
    
    if select==1:
        print("creat ERPe your acc")
        name=str(input("enter your name:"))
        phone_no=int(input("enter your 10 digit number:"))
        dob=str(input("enter your DOB in dd-mm-yyyy format:"))
        password=str(input("create strong password using @#&:"))
        roll_no=str(input("enter your roll_no:"))
        userdefine(name,phone_no,dob,password,roll_no)
        
    if select==2:
        print("login into existing acc")
        roll_no=str(input("enter your roll no:"))
        password=str(input("enter your ERP password"))
        login(roll_no,password)
        
    if select==3:
        roll_no=str(input("enter your roll number:"))
        print("if you want to unchange the details press enter key ,\n if you want change the details type details in required text area")
        name=str(input("enter your name:"))
        phone_no=str(input("enter your 10 digit number:"))
        dob=str(input("enter your DOB in dd-mm-yyyy format:"))
        password=str(input("create strong password using @#&:"))
        uprate(roll_no,name,phone_no,dob,password)

    if select==4:
        roll_no=str(input("enter your roll number"))
        if roll_no  in ERP:
            for j in ERP[roll_no].keys():
                print(j,"=",ERP[roll_no][j])
            print("succussfully display the details")
        else:
            print("account is not found")
    if select==5:
        roll_no=str(input("enter your roll number"))
        if roll_no in ERP:
            ERP.pop(roll_no)

    if select==6:
        print("successfully logout")
        break
    
        
        
              
        
    
