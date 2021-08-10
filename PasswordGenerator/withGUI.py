"""
GUI version of the password generator.
generates the password in file password.txt.
You can refer my encryption repo to encrpyt that password thanks.
"""

from tkinter import *
import random
import os


master = Tk()
master.title("Password Generator")
master.geometry("300x400")

Label(master, text='Number of password').grid(row=0)
numPass = Entry(master, width = 35,borderwidth = 5)
numPass.grid(row=0, column=1, padx=10, pady=5)

Label(master, text='Password length').grid(row=1)
lenPass = Entry(master, width = 35,borderwidth = 5)
lenPass.grid(row=1, column=1, padx=10, pady=5)

# creating the password file

pass_file = open("password.txt","a")

def generatePass():
    char_domain = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    n = int(numPass.get())
    p = int(lenPass.get())

    for i in range(n):
        password = ""
        for j in range(p):
            password += random.choice(char_domain)

        pass_file.write(password)

 

Button(master, text ="Generate",height = 2,width = 10,command=generatePass).grid(row=2,column=1)

master.mainloop()
