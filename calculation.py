try:
    x=int(input("enter the 1st number:"))
    y=int(input("enter the 2nd number:"))
    z=str(input("enter the operator symbol:"))
    if z!="/":
        raise Exception(" pls make sure the entered symbol")
    elif x==0:
        raise Exception(" anything by zero is one")
    elif y==1:
        raise Exception(" make sure the number")
    elif z=="/":
        print("anwer", x/y)
except ValueError:
    print("pls enter number value")
except ZeroDivisionError:
    print(" do not enter zero")
except Exception as e:
    print(f"something went wrong:(e)")
finally: 
    print("calculation is completed")

    


