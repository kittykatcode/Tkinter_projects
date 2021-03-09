from tkinter import *
from PIL import ImageTk,Image


root= Tk()
root.title('Learning about Radio Buttons')


#r= IntVar()
#r.set(20) #for placing an alreaded selected 

M= [('pizza', 20),('tikki',10),('aloo',5),('puri',2)]

chaat = IntVar() #declaring if its an int or str

#creating radio button with a loop
for k,v in M:
    Radiobutton(root,text=k,variable=chaat, value=v).pack() 
#creating a click button
def clicked(value):
    lable_1= Label(root, text=chaat.get()).pack()
 

#creating radio buttons
#Radiobutton(root,text='Opt-1', variable=r, value=50, command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text='Opt-2', variable=r, value=20,command=lambda: clicked(r.get())).pack()

b2= Button(root,text='click!',command=lambda: clicked(chaat.get())).pack()
b= Button(root, text='close', command=root.quit, bg='red').pack(anchor=E)

#lable_1= Label(root, text=r.get()).pack()
root.mainloop()