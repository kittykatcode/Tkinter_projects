from tkinter import *

window=Tk()
window.title("tkinter lecture from : The python Mega course")


def km_to_m():
    t1.delete('1.0','end') # to delete last excution and clear the text box
    miles = float(e1.get())*1.60 # e1.get is an int which can not be multiplyied with a float thus we need to convert e1.get into a float
    t1.insert(END,miles) # have to addEND to add the text at the end of the block





#create a button called execute
b1=Button(window,text='Excecute', command=km_to_m)
b1.grid(row=0,column=0)


#create an entry widget
e1 = Entry(window)
e1.grid(row=0,column=1)

#create a text widget, 
# default text widget is quite big, but we can customise it by specifing height and width
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)



window.mainloop()