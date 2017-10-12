#!/usr/bin/python
from Tkinter import *
import Tkinter

root = Tkinter.Tk()
# Code to add widgets will go here...
frame = Tkinter.Frame(root)
frame.pack()
var = StringVar()
label = Label( frame, textvariable=var , font = 35)
var.set("Enter the query here : ")

label.pack()
root.mainloop()