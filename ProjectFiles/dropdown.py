from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title('Drop Down Boxes')
root.geometry('700x700')

def show():
    Label(root, text= c.get()).pack()

day= ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']
c= StringVar()
c.set(day[-1])
drop = OptionMenu(root, c, *day).pack() # put * if want to access the list or pass the entire list seperated by ','

Button(root, text='Show selection', command= show).pack()

root.mainloop()