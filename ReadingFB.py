import pyrebase
from pprint import pprint
import json

import tkinter


#pip install pyrebase4

config = {
  "apiKey": "m2YYSDBUFvfB3AU7Px2mMoHtTUwRDOZhce6hgC38",
  "authDomain": "temperatureproject-666.firebaseio.com",
  "databaseURL": "https://temperatureproject-666.firebaseio.com/",
  "projectID": "temperatureproject-666",
  "storageBucket": "temperatureproject-666",
}
# Ctrl+K+C, you'll comment out the section of code. Ctrl+K+U will uncomment the code
# https://stackoverflow.com/questions/57256408/how-can-i-get-a-key-from-the-value-in-firebase
firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

db = firebase.database()

DateYearDay =  db.child("DHT").get()

for paiva in DateYearDay.each():
    datetimes = paiva.val()

    for klo in datetimes:
        
        temp = datetimes[klo]["Temp"]
        humid = datetimes[klo]["Humid"]
        lampotilakatsaus = "{0} | {1} | {2}°C | {3}%"
        print(lampotilakatsaus.format(paiva.key(),klo,temp,humid))
        #print(paiva.key(),klo,temp,humid)
    

#Tästä eteenpäin mars
