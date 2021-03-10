from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title('Weather Reort')
root.geometry('400x80')

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=180CA08A-06FF-4946-BDDC-381FEF06ABD0

#Zip Code lookup Fun

def ZipLookUp():
    try:
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get()+"&distance=25&API_KEY=180CA08A-06FF-4946-BDDC-381FEF06ABD0")
        x = json.loads(api_requests.content)
        city = x[0]["ReportingArea"]
        Category = x[0]["Category"]['Name']
        Quality= str(x[0]['AQI'])

        if Category == "Good":
            bg_color = 'green'
        elif Category == 'Moderate':
            bg_color = 'yellow'
        elif Category == 'Unhealthy for Sensitive Groups':
            bg_color = 'orange'
        elif Category == 'Unhealthy':
            bg_color = 'red'
        elif Category == 'Very Unhealthy':
            bg_color = 'purple'
        elif Category == 'Hazardous':
            bg_color = 'maroon'

        root.configure(background= bg_color)


        DataLable=Label(root, text= city + ' Air Quality : ' + Quality  + ' '+ Category, font=("Helvetica",18), background= bg_color ).grid(row=1,column=0,columnspan=2)
        
    except Exception as e:
        x = 'errorr.....'
    



zip = Entry(root)
zip.grid(row=0,column=0, sticky= W+E+N+S)
Button(root, text="look UP : Zip", command=ZipLookUp).grid(row=0,column=1,sticky= W+E+N+S)

root.mainloop()