m1=[]
row=int(input("enter the number of row:"))
column=int(input("enter the number of column:"))
print("matrix 1")
for i in range(row):
    r=[]
    for j in range(column):
        u=int(input("enter the numbers in list"))
        r.append(u)
    m1.append(r)
for i in m1:
    print(i)
m2=[]
for i in range(row):
    r=[]
    for j in range(column):
        u=int(input("enter the number in list"))
        r.append(u)
    m2.append(r)
for i in m2:
    print(i)
m3=[]
for i in range(row):
    r=[]
    for j in range(column):
        sub=m1[i][j]-m2[i][j]
        r.append(sub)
    m3.append(r)
for i in m3:
    print(i)
              
