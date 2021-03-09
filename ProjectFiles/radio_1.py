from tkinter import *
from PIL import ImageTk,Image


root= Tk()
root.title('Learning about Radio Buttons')


#r= IntVar()
#r.set(20)

M= ('pizza', 'tikki','aloo','puri')

chaat = StringVar()

for k in M:
    Radiobutton(root,text=k,variable=chaat, value=k).pack() # works in simple list too
def clicked(value):
    lable_1= Label(root, text=chaat.get()).pack()
 


#Radiobutton(root,text='Opt-1', variable=r, value=50, command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text='Opt-2', variable=r, value=20,command=lambda: clicked(r.get())).pack()

b2= Button(root,text='click!',command=lambda: clicked(chaat.get())).pack()
b= Button(root, text='close', command=root.quit, bg='red').pack(anchor=E)

#lable_1= Label(root, text=r.get()).pack()
root.mainloop()