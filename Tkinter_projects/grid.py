from tkinter import *

root = Tk()

#creating a Lable widget
myLable0 = Label(root, text='Hello World!')
myLable1 = Label(root, text='I am Iron Man!')
myLable2 = Label(root, text=" ' ")

#putting it on to the screen
myLable0.grid(row=0, column=0)
myLable1.grid(row=1, column=7)
myLable2.grid(row=1, column=1)


#looping to k ow where the cursor at
root.mainloop()