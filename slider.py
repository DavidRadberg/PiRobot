from tkinter import *
import time



x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0


def show_values():
    print (w1.get(), w2.get(), w3.get(), w4.get(), w5.get(), w6.get(), )
    

def update_values():
    global x1
    global x2
    global x3
    global x4
    global x5
    global x6
    x1 = w1.get()
    x2 = w2.get()
    x3 = w3.get()
    x4 = w4.get()
    x5 = w5.get()
    x6 = w6.get()

master = Tk()
w1 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w1.set(0)
w1.pack()
w2 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w2.set(0)
w2.pack()
w3 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w3.set(0)
w3.pack()
w4 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w4.set(0)
w4.pack()
w5 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w5.set(0)
w5.pack()
w6 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w6.set(0)
w6.pack()
Button(master, text='Show', command=show_values).pack()
Button(master, text='Update', command=update_values).pack()

x = 0

while True:
    x = x+1
    if(x % 5000 == 0):
        print(x1, x2, x3, x4, x5, x6)
    master.update_idletasks()
    master.update()
    
    





    
