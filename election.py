name=str(input("enter your name:"))
age=int(input("enter your age:"))
country=str(input("enter your nation:"))
file_n=str(input("enter the for ur file:"))
f=open(file_n,"w+")
if age>18 and country.strip().lower()=="india":
    f.write(f"hi {name.title()} your elible to vote")
else:
    f.write(f"hi {name} your not elible to vote")
f.seek(0)
print(f.read())
f.close()
