'''m =[]
row_no=int(input("enter the number of rows"))
column_no=int(input("enter the nimber of column"))
for i in range(row_no):
    for j in range(column_no):
        L1=int(input("enter the value:"))
        m[i][j]=L1
for i in range(len(m)):
        print(m[i])
'''
m1=[]
row=int(input("enter the number of rows:"))
column=int(input("enter the number of column:"))
print("matrix 1")
for i in range(row):
    r=[]
    for j in range(column):
        u=int(input("enter the list values"))
        r.append(u)
    m1.append(r)
for i in m1:
    print(i)
m2=[]
print("matrix2")
for i in range(row):
    r=[]
    for j in range(column):
        u=int(input("enter the list values"))
        r.append(u)
    m2.append(r)
for i in m2:
    print(i)
sum=[]
for i in range(row):
    r=[]
    for j in range(column):
        add=m1[i][j]+m2[i][j]
        r.append(add)
    sum.append(r)
print(sum)
for i in sum:
    print(i)


