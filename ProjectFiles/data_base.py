from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()
root.title('Databases SQLight')
root.geometry('400x400')

#Database

# Create a Database or connect to one
con = sqlite3.connect('Address_book.db')

# create the cursoor.. cursor is the one which connects to the database and does stuff for us
c= con.cursor()
# create table of database
#5 data types for sqlite: text, integer,real,null,blob
#c.execute("""CREATE TABLE addressess (
#    first_name text,
#    second_name text,
#    street_name text,
#    city text,
#    Zip_code integer)""")
#create submit function

#function to delete record
def delete_record():
    # Create a Database or connect to one
    con = sqlite3.connect('Address_book.db')
    # create the cursoor.. cursor is the one which connects to the database and does stuff for us
    c= con.cursor()
    #inserting into database table
    c.execute("DELETE from addressess WHERE oid = "+  delete_box.get())

    delete_box.delete(0,END)


    # commit changes to database
    con.commit()

    #end /close database connection
    con.close()


def submit():
    # Create a Database or connect to one
    con = sqlite3.connect('Address_book.db')
    # create the cursoor.. cursor is the one which connects to the database and does stuff for us
    c= con.cursor()
    #inserting into database table
    c.execute("INSERT INTO addressess VALUES (:f_name, :s_name, :address, :city, :z_code)",
            {
            "f_name": f_name.get(),
            "s_name": s_name.get(),
            "address": address.get(),
            "city": city.get(),
            "z_code": z_code.get()
            })

    # commit changes to database
    con.commit()

    #end /close database connection
    con.close()
    #clear boxes
    f_name.delete(0,END)
    s_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    z_code.delete(0,END)

# query function to get data 
def query_btn():
    # Create a Database or connect to one
    con = sqlite3.connect('Address_book.db')
    # create the cursoor.. cursor is the one which connects to the database and does stuff for us
    c= con.cursor()
    #inserting into database table
    c.execute("SELECT *,oid FROM addressess")
    records = c.fetchall()
    #print(records)
    # looping through the result 
    print_rec = ''
    for record in records:
        print_rec += str(record[5])+'\t'+str(record[0])+' '+str(record[1])+'\n' 

    Lable_record=Label(root, text= print_rec)
    Lable_record.grid(row=10,column=0,columnspan=2, sticky=W)



    # commit changes to database
    con.commit()

    #end /close database connection
    con.close()
    #clear boxes
    
#Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=10, pady=(10,0))
s_name = Entry(root, width=30)
s_name.grid(row=1,column=1, padx=10)
address = Entry(root, width=30)
address.grid(row=2,column=1, padx=10)
city = Entry(root, width=30)
city.grid(row=3,column=1, padx=10)
z_code = Entry(root, width=30)
z_code.grid(row=4,column=1, padx=10)
#delete box
delete_box= Entry(root, width=30)
delete_box.grid(row=7,column=1,padx=10)

#Create lables
Label(root,text='First Name').grid(row=0,column=0,pady=(10,0))
Label(root,text='second Name').grid(row=1,column=0)
Label(root,text='Street Name').grid(row=2,column=0)
Label(root,text='City ').grid(row=3,column=0)
Label(root,text='Zip Code').grid(row=4,column=0)
Label(root,text='ID number').grid(row=7,column=0)


#Create submit button
Button(root,text='add Data to the database', command=submit, bd=2).grid(row=5,column=0,columnspan=2, padx=20,ipadx=100)

#Query button
Button(root,text='Show Records', command=query_btn,bd=2).grid(row=6,column=0,columnspan=2 ,ipadx=137)
#button for deleting records
Button(root, text='Delete Records', command=delete_record, bd=2).grid(row=8,column=0,columnspan=2,ipadx=136)
# commit changes to database
con.commit()

#end /close database connection
con.close()
root.mainloop()
