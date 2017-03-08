#!/usr/bin/python
from Tkinter import *

def square():
	square=float(num.get())**2
	num.delete(0,END)
	num.insert(0,square)

def selfmulti():
	read=float(num.get())
	num.delete(0,END)
        num.insert(0,read*read)

def clearall():
	num.delete(0,END)

def quit():
	root.destroy()

root=Tk()
root.title('Hello')
mwindow = Frame(root)
mwindow.pack()
bt1=Button(mwindow, text = 'Clear', fg='red',bg='blue',command =clearall)
bt1.pack()
bt2=Button(mwindow, text = 'Button2', fg='blue',bg='red')
bt2.pack()
bt3=Button(mwindow, text = 'Button3', fg='yellow',bg='green')
bt3.pack()
bt4=Button(mwindow, text = 'Button4', fg='green',bg='yellow')
bt4.pack()
bt5=Button(mwindow, text = 'multiself', fg='black',bg='white', command=selfmulti)
bt5.pack()
bt6=Button(mwindow, text = 'Square', fg='white',bg='black', command=square)
bt6.pack()
bt7=Button(mwindow, text = 'Quit', fg='cyan',bg='grey', command=quit)
bt7.pack()
num=Entry(root)
num.pack()

root.mainloop()
