from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('light_bulb_copy.ico')


my_img = ImageTk.PhotoImage(Image.open('lotus.jpeg'))
my_lable = Label(image= my_img).pack()
#my_lable.pack()

button_quit = Button(root, text='quit the program', command=root.quit).pack()



root.mainloop()
