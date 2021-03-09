from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('light_bulb_copy.ico')


my_img1 = ImageTk.PhotoImage(Image.open('Images/lotus.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/bouque.jpeg'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/cat.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/daisy.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open('Images/img_1.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('Images/logo.jpeg'))
my_img7 = ImageTk.PhotoImage(Image.open('Images/rose.jpeg'))

# putting all the images in a list to be able to access them easily
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]


my_lable = Label(image= my_img1)
my_lable.grid(row=0, column=0, columnspan=3)
#my_lable.pack()
# creating status bar at the bottom to know which picture we are on
# sticky : going from West to East
#anchor : anchoring text towards East ( right hand side)
staus_bar = Label(root, text= 'Image 1 of'+ str(len(img_list)),relief=SUNKEN, bd=1, anchor=E)
staus_bar.grid(row=2,column=0,columnspan=3, sticky=W+E)

def forward_button(img_num):
    global my_lable
    global button_forward
    global button_back

    my_lable.grid_forget() #to remove or forgetthe current image
    my_lable = Label(image =img_list[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward_button(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back_button(img_num-1))

    # disabling forward button on last image
    if img_num == len(img_list):
        button_forward = Button(root, text='>>', state=DISABLED)

    # updating status bar with every forward click
    staus_bar = Label(root, text= 'Image ' +str(img_num) + ' of'+ str(len(img_list)),relief=SUNKEN, bd=1, anchor=E)
    staus_bar.grid(row=2,column=0,columnspan=3, sticky=W+E)

    my_lable.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def back_button(img_num):
    global my_lable
    global button_forward
    global button_back

    my_lable.grid_forget() #to remove or forgetthe current image
    my_lable = Label(image =img_list[img_num-1])
    button_forward = Button(root, text='>>', command=lambda: forward_button(img_num+1))
    button_back = Button(root, text='<<', command=lambda: back_button(img_num-1))
    # Disabling back button for the 1st pic
    if img_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)
    #updating status bar
    staus_bar = Label(root, text= 'Image ' +str(img_num) + ' of'+ str(len(img_list)), relief=SUNKEN, bd=1, anchor=E)
    staus_bar.grid(row=2,column=0,columnspan=3, sticky=W+E)

    my_lable.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


  # buttons to navigate att he bottom  
button_quit = Button(root, text='quit the program', command=root.quit).grid(row=1, column=1, pady=10)
button_back = Button(root, text='<<', command=lambda: back_button()).grid(row=1, column=0)
button_forward = Button(root, text='>>', command=lambda: forward_button(2)).grid(row=1, column=2)





root.mainloop()
