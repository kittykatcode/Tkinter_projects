from tkinter import *

root=Tk()

e = Entry(root)
e.pack()
e.insert(0,'enter your name')

def myclick():
    greeting = 'Hello ' + e.get() + ' , How are you today?'
    mylable = Label(root, text=greeting)
    mylable.pack()

mybutton = Button(root, text='Enter your name', command=myclick)
#SHORTER WAY OF RIITING SAME THING
#mybutton = Button(root, text='Click me').pack()

mybutton.pack()


root.mainloop()