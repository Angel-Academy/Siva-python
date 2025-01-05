import sqlite3
import tkinter as tk
conn=sqlite3.connect('account.db')
cur=conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS login(
id INTEGER PRIMARY KEY AUTOINCREMENT,
phone_no INTERGER NOT NULL,
password TEXT NOT NULL)''')
conn.commit()
conn.close()
def login():
    phone_num=phtext.get()
    passcord=passtext.gettext()
    cur.execute(''' SELECT * FROM login WHERE phone =? AND password =?''',(phone_no,password))
    detail=cur.fetchone()
    if detail:
        massage.config(root,text="succussfully login",bg="green",fg="black",font=("ariel",20))
    else:
        massage.config(root,text="password incorrect",bg="red",fg="black",font=("ariel",20))
def signup():
    phone=phtext.get()
    passcord=passtext.get()
    if phone_num and passcord:
        try:
            cur.execute(''' INSTERT INTO login (phone_no,password) VALUES(?,?)''',(phone_no,password))
            conn.commit()
            massage.config(root,text="YOUR ACC IS CREATED",bg="green",fg="black",font=("ariel",20))
        except sqlite3.IntegrityError:
            massage.config(root,text="already existing",bg="red",fg="black",font=("ariel",20))
            
    else:
        massage.config(root,text="insure all textbox",bg="red",fg="black",font=("ariel",20))
def forgot():
    pass
root=tk.Tk()
root.title("login")
root.geometry("900x400")
root.config(bg="pink")

title=tk.Label(root,text="INSTAGRAM LOGIN",bg="pink",fg="blue",font=("ariel",20))
title.pack()
phone=tk.Label(root,text="REGISTER NUMBER",bg="pink",fg="blue",font=("ariel",10))
phone.pack()
phtext=tk.Entry(root)
phtext.pack()
password=tk.Label(root,text="ENTER PASSWORD",bg="pink",fg="blue",font=("ariel",10))
password.pack()
passtext=tk.Entry(root)
passtext.pack()
loginbtn=tk.Button(root,text="LOGIN",bg="pink",command=login)
loginbtn.pack()
siginbtn=tk.Button(root,text="SIGN IN",bg="pink",command=signup)
siginbtn.pack()
forgotbtn=tk.Button(root,text="FORGOT PASSWORD",bg="pink",command=forgot)
forgotbtn.pack()
massage=tk.Label(root,text="",bg="pink",fg="blue",font=("ariel",10))
massage.pack()
root.mainloop()
 
