"""x=int(input("enter number :"))
y=int(input("enter number :"))
z=int(input("enter number :"))
if x>y and x>z:
    print(f"{x}-x")
elif y>x and y>z:
    print(f"{y}-y")
elif z>x and z>y:
    print(f"{z}-z")
else:
    print(x,y,z)
#checking letters wheater vowel or consonant
letter=str(input("enter the letters from A TO Z:")).lower()
if letter == "a" or letter == "e" or letter =="i" or letter =="o" or letter =="v":
    print("entered letter is a vowel")
else:
    print("entered letter is a consonant")
#creating tables using for loop

table=int(input("enter the number u want :"))
for i in range(1,11):
    print(f"{table} X {i} = {table*i}")
"""
l=[1,5,6,7,8,3,4]
l.append(6)
n=l[-1::-1]
print(l.index(6))
    
