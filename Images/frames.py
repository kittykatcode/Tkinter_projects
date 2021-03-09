from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("learning about addind frames")

frame_1= LabelFrame(root, text='this is my frame',padx=50,pady=20, bg='gray') #creating a frame
frame_1.grid(row=0, column=0,padx=100, pady=100)# putting the frame on the screen

frame_2= LabelFrame(root, text='Quit',padx=20,pady=20, bg='red') #creating a frame
frame_2.grid(row=1, column=1,padx=20, pady=20, sticky=E+W)# putting the frame on the screen


b_1= Button(frame_1,text='useless button').grid(row=0,column=0) # creating a button in frame_1
b_2=  Button(frame_1,text='another button').grid(row=1,column=1) # creating another button in frame_1
b_3= Button(frame_2,text="X", command= root.quit,).pack()

# even though frame is .pack in root, we can use .grid inside of frame or vise-versa


root.mainloop()