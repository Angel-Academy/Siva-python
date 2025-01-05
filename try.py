
try:
    age=int(input("enter the age:"))
    x="2"
    if not type(x) is int:
        raise Exception("TypeError")
except Exception as e:
    print(f"something went wrong:{e}")
except:
    print("ValueEror")

finally:
    print("completed")
