#import packages
from tkinter import *
import time



#initialize values
x1 = 0
x2 = 0
x3 = 0
x4 = 255
x5 = 255
x6 = 255


#define functions
def show_values():
    print(w1.get(), w2.get(), w3.get(), w4.get(), w5.get(), w6.get())

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
