from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox

root= Tk()
root.title('Learn to build message box')

def popup():
    #error = messagebox.showerror("error", "It will show error here") #returns OK
    #info = messagebox.showinfo("info", 'this will show info') #returns OK
    #warning = messagebox.showwarning("warning", 'this will warning info') #returns OK
    #ask = messagebox.askquestion("askquestion", 'this will question info') #returns yes and no
    #askcancel = messagebox.askokcancel("askok to cancel", 'this will ask to cancel info') #returns 0 &1
    askyn = messagebox.askyesno("yn", "Is Vader Luke's dad?")  #returns 0 &1
    Label(root,text=askyn).pack()
    if askyn == 1:
        Label(root,text="You are right!").pack()
    else:
        Label(root,text="NOOOOOOOOOOO").pack()




    # showinfo,showwarning,showerror,askquestion,askokcancel,askyesno

b = Button(root, text="Clickity click!", command= popup).pack()


root.mainloop()