from tkinter import*
from PIL import ImageTk, Image
import numpy as np 
import matplotlib.pyplot as plt 



root=Tk()
root.title('Charts')
root.geometry('400x200')

def graph():
    #creating data with numpy : 5000 data with average of 200000 and standard deviation is 25000
    house_price = np.random.normal(200000,25000,5000)
    # creating  a histagram(bar chart) 50 bars with matplotlip.pyplot
    plt.hist(house_price,50) # this will reate graph but will not show
    plt.show()# this will show graph

Button(root, text='click to see graph', command=graph).pack()

root.mainloop()

