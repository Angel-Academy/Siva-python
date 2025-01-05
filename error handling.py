'''
try:
    print(y)
except:
    print("hi")
else:
    print("printed")
finally:
    print("try..catch")
print("end")
l=[1,3,2,2,3]
try:
    l.pop(5)
    print(l)
except AttributeError:
    print("enter the crt attribute")
except IndexError:
    print("enter the crt index value")
else:
    print("successfully")
finally:
    print("checking try catch")
'''    
x=20
try:
    if x==20:
        raise Exception("number is 20 try differnet number")
        
    print(l)
    raise TypeError("enter the value")
except AttributeError:
    print("enter the crt attribute")
except IndexError:
    print("enter the crt index value")
else:
    print("successfully")
except Exception as e:
    print(f"something went wrong:(e)")
finally:
   print("checking try catch")
