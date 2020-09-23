# Weather App that provides you the temperature and timezone details of a city on a click

from tkinter import *
import requests
import json


root = Tk()
root.title("Weather App")
root.iconbitmap('disneyland.ico')
root.geometry("600x200")
root.configure(background="White")


api_p1 = "https://api.weatherbit.io/v2.0/current?city="
api_p2 = ",IN&key=" #Add your own key here

def submit():
    try:
        api_rq = requests.get(api_p1+ent.get()+api_p2)
        api = json.loads(api_rq.content)
        ap = api["data"]

        mylbl1 = Label(root, background="White", padx=70, text="City : " + str(ap[0]['city_name']), font=("Helvetica", 20))
        mylbl1.pack()

        mylbl2 = Label(root, background="White", padx=3, text="TimeZone : " + str(ap[0]['timezone']),
                       font=("Helvetica", 20))
        mylbl2.pack()

        mylbl3 = Label(root, background="White", padx=5, text="Temperature : " + str(ap[0]['temp']) + " deg C",
                       font=("Helvetica", 20))
        mylbl3.pack()

    except Exception as e:
        api = "Error"


mylbl = Label(root, background="SkyBlue", padx=70, text="Enter City Name : ", font=("Helvetica", 20))
mylbl.pack()

ent = Entry(root, background="White", borderwidth=3, font=("Helvetica", 20))
ent.pack()

btn = Button(root, text="Search", font=("Helvetica", 20), command=submit)
btn.pack()

root.mainloop()
