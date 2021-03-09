from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("CheckBoxes")
root.geometry('400x400')

def show():
    Label(root,text=v.get()).pack()

v= StringVar()

c= Checkbutton(root, text='Please check me!', variable=v, onvalue='ON', offvalue='Off')
c.deselect() # will de select the box
c.pack()
# Defaultcheckbox gets response in the form of 0&1, 0 if unchecked , 1 if checked
#this can be chenged by using Onvalue : if box is checked & offvalue: if the box is not checked in

Button(root, text="show slection", command= show).pack()

root.mainloop()