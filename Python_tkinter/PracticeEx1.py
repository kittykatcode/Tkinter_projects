from tkinter import *

root= Tk()
root.title("Conver kg to gm and ounce")



def conv():
    try:
        t1.delete('1.0','end')
        t2.delete('1.0','end')
        t3.delete('1.0','end')
        v = int(e.get())
        kg_gm = v*1000
        kg_Pound = float(v)*2.205
        kg_ounce = float(v)*35.274
        t1.insert(END,kg_gm)
        t2.insert(END,kg_Pound)
        t3.insert(END,kg_ounce)
    except Exception : # if entered text is not an int
        e.delete(0,END)
        e.insert(END,"Please write a num")




l1=Label(root, text= 'Enter KG',).grid(row=0,column=0)
e= Entry(root, )
e.grid(row=0,column=1)
b1= Button(root, text='convert', command=conv)
b1.grid(row=0,column=2)
t1= Text(root, height=1,width=10)
t1.grid(row=1,column=0)
t2= Text(root, height=1,width=10)
t2.grid(row=1,column=1)
t3= Text(root, height=1,width=10)
t3.grid(row=1,column=2)

root.mainloop()