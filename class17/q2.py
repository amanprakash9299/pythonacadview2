import tkinter
from tkinter import *
import sys

def show():
	print("Hello World!")
	
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

b=Button(root,text="click!",width=20,bg='red',command=show)
b.place(x=50,y=50)
