from datetime import *
import tkinter
import tkinter.font as tkFont
from tkinter import *
from pytz import timezone
import sys
import os

def restart_program():
    print("program should restart now")
    python = sys.executable
    os.execl(python, python, * sys.argv)

def changeCEST():
    b = Button(root, text="Back", bg="green",command=restart_program)
    b.place(relx=.43, rely=.5, anchor="center")
    CEST = Button(root, text="CEST", bg="blue")
    germany = timezone('Europe/Berlin')
    a = datetime.now().astimezone(germany)
    currentTime = a.strftime("%H:%M:%S")
    w.config(text=currentTime)
    root.after(1000, changeCEST)

def changeGMT():
    b = Button(root, text="Back", bg="green",command = restart_program)
    b.place(relx=.43, rely=.5, anchor="center")
    england = timezone('Europe/London')
    a = datetime.now().astimezone(england)
    currentTime = a.strftime("%H:%M:%S")
    w.config(text=currentTime)
    root.after(1000, changeGMT)

def changeEST():
    b = Button(root, text="Back", bg="green",command = restart_program)
    b.place(relx=.43, rely=.5, anchor="center")
    eastern = timezone('US/Eastern')
    a = datetime.now().astimezone(eastern)
    currentTime = a.strftime("%H:%M:%S")
    w.config(text=currentTime)
    root.after(1000, changeEST)

def changeCST():
    b = Button(root, text="Back", bg="green",command = restart_program)
    b.place(relx=.43, rely=.5, anchor="center")
    central = timezone('US/Central')
    a = datetime.now().astimezone(central)
    currentTime = a.strftime("%H:%M:%S")
    w.config(text=currentTime)
    root.after(1000, changeCST)


root = Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=70)
buttonFont = tkFont.Font(family="Lucida Grande", size=20)
w = Label(root, text=".", fg="green",bg = "black", font=fontStyle)
w.pack()
GMT = Button(root, text="GMT", bg="blue",command = lambda: changeGMT())
GMT.place(relx=.43, rely=.3, anchor="center")
GMT['font'] = buttonFont
CEST = Button(root, text="CEST", bg="blue",command = lambda: changeCEST())
CEST.place(relx=.25, rely=.3, anchor="center")
CEST['font'] = buttonFont
EST = Button(root, text="EST", bg="blue",command = lambda: changeEST())
EST.place(relx=.59, rely=.3, anchor="center")
EST['font'] = buttonFont
CST = Button(root, text="CST", bg="blue",command = lambda: changeCST())
CST.place(relx=.75, rely=.3, anchor="center")
CST['font'] = buttonFont

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
w.config(text=currentTime)
root.after(1000)

root.geometry("600x600")
root.mainloop()
