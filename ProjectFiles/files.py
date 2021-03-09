from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog

root = Tk()
root.title("Open files")

# getting an error : not fetching the acctual file path 
#root.filename = filedialog.askopenfile(initialdir='Images', title='select a file', filetypes=(('jpg files', '*.jpg'),('jpeg files', '*.jpeg'),('all files','*.*')))
#lbl = Label(root, text= root.filename).pack()
#img = ImageTk.PhotoImage(Image.open(root.filename))
#l = Label(root,image=img).pack()


def Open():
    global img
    root.filename = filedialog.askopenfile(initialdir='Images', title='select a file', filetypes=(('jpg files', '*.jpg'),('jpeg files', '*.jpeg'),('all files','*.*')))
    lbl = Label(root, text= root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename[1]))
    l = Label(root,image=img).pack()

btn = Button(root, text='Open File', command=Open).pack()


root.mainloop( )
