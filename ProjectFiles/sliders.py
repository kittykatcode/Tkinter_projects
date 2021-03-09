from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Slider')
root.geometry('400x400') # specifing how big window we want


def slide(var):
    Lbl = Label(root, text=Hrozontal_slider.get()).pack()
    root.geometry(str(Hrozontal_slider.get())+'x'+str(verti_slider.get()))


verti_slider = Scale(root, from_=0, to=200)
verti_slider.pack()
#verti_slider = Scale(root, from_=0, to=200)
#verti_slider.pack()

Hrozontal_slider = Scale(root, from_=100, to=400, orient=HORIZONTAL, command=slide)
Hrozontal_slider.pack()
Lbl = Label(root, text=Hrozontal_slider.get()).pack()


btn = Button(root, text='Click', command= slide).pack()

root.mainloop()