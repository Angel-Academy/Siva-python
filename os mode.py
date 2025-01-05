import os
#print(os.getcwd())
#os.rmdir("python")
#os.mkdir("python")
#os.chdir("python")
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())
os.path.exists("python")
print(os.getcwd())
if os.path.exists("python"):
    os.rmdir("python")
else:
    os.mkdir("python")
    os.chdir("python")
print(os.getcwd())
