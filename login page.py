
import os
import webbrowser
if not(os.path.exists("login")):
    #os.rmdir("login")
    os.mkdir("login")
print(os.getcwd())
os.chdir("login")
print(os.getcwd())
username="sanjay"
passcode="sanjay@123"
uname=str(input("enter the username:"))
password=str(input("enter the password:"))
file_name=str(input("enter the file name with (.html)extention:"))
f=open(file_name,"w")
if uname==username and password==passcode:
    f.write('''<html>
<head>
<title>login</title>
</head>
<body>
<h1 style="color:red;"> <center> INSTAGRAM </h1>
<p style="color:blue;"> login successfully </p>
</body>
</html>''')
elif uname!=username and password!=passcode:
    f.write('''
<html>
<head>
<title>login</title>
</head>
<body>
<h1 style="color:red;"> <center> INTSAGRAM </h1>
<p style="color:blue;"> login failed </p>
</body>
</html>''')
webbrowser.open(file_name)
f.close()

          
