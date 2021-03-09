from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog

root = Tk()
root.title("Open files")

root.filename = filedialog.askopenfile(initialdir='Images', title='select a file', filetypes=(('jpg files', '*.jpg'),('jpeg files', '*.jpeg'),('all files','*.*')))
lbl = Label(root, text= root.filename).pack()
#img = ImageTk.PhotoImage(Image.open(root.filename))
#l = Label(root,image=img).pack()

root.mainloop( )
