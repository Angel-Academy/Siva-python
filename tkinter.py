import tkinter as tk
root=tk.Tk()
root.title("login")
root.geometry("900x400")
root.config(bg="pink")

title=tk.Label(root,text="INSTAGRAM LOGIN",bg="pink",fg="blue",font=("ariel",20))
title.pack()
phone=tk.Label(root,text="REGISTER NUMBER",bg="pink",fg="blue",font=("ariel",10))
phone.pack()
phtext=tk.Text(root,width=20,height=1)
phtext.pack()
password=tk.Label(root,text="ENTER PASSWORD",bg="pink",fg="blue",font=("ariel",10))
password.pack()
passtext=tk.Text(root,width=20,height=1)
passtext.pack()
loginbtn=tk.Button(root,text="LOGIN",bg="pink",command=login)
loginbtn.pack()
siginbtn=tk.Button(root,text="SIGN IN",bg="pink",command=signup)
siginbtn.pack()
forgotbtn=tk.Button(root,text="FORGOT PASSWORD",bg="pink",command=forgot)
forgotbtn.pack()
root.mainloop()
