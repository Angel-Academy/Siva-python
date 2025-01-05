import random as rd
x = rd.randint(1000 , 10000)
print(x)
color=["pink " , "orange","yellow"]
x = rd.choice(color)
print(x)
rd.shuffle(color)
print(color)
