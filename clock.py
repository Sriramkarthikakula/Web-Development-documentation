from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("clock")
def time():
    string = strftime("%d/%B/%Y \n %H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
