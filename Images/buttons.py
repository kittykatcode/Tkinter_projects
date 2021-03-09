from tkinter import *

root = Tk()


def myclick():
    mylable = Label(root, text="i clicked a button", fg='green').pack()

mybutton = Button(root, text='Click me', command=myclick , fg='black', bg='red')
#SHORTER WAY OF RIITING SAME THING
#mybutton = Button(root, text='Click me').pack()

mybutton.pack()



root.mainloop()