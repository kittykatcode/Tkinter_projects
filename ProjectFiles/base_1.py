from tkinter import *
from PIL import ImageTk, Image

root =Tk() # you dont want to run more than one Tk()
root.title('New Window')

def open_window():
    global img # image will not load in 2nd window if this is not global
    top = Toplevel() # to open 2nd window in Tkinter
    top.title("This is new Window")
    img = ImageTk.PhotoImage(Image.open('Images/daisy.jpeg'))
    lbl= Label(top, image=img).pack()
    Button(top, text='QUIT', command=top.destroy).pack(anchor=E) # .quit will close entire function, .destory will only close this window



Button(root, text='clickity click!', command=open_window).pack()




root.mainloop()

