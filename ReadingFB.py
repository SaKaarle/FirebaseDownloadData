import pyrebase
from pprint import pprint
import json

import tkinter
import firebase_admin
from firebase_admin import credentials


#pip install pyrebase4

config = {
  "apiKey": "AIzaSyC0gWWH779wuS1c8NuDHPF4TgwfcmlX5WQ",
  "authDomain": "temperatureproject-666.firebaseio.com",
  "databaseURL": "https://temperatureproject-666.firebaseio.com/",
  "projectID": "temperatureproject-666",
  "storageBucket": "temperatureproject-666",
}
# Ctrl+K+C, you'll comment out the section of code. Ctrl+K+U will uncomment the code
# https://stackoverflow.com/questions/57256408/how-can-i-get-a-key-from-the-value-in-firebase
firebase = pyrebase.initialize_app(config)

cred = credentials.Certificate('F:/code/Firebase/temperatureproject-666-firebase-admin.json')
default_app = firebase_admin.initialize_app(cred,
{'databaseURL': 'https://temperatureproject-666.firebaseio.com/'})

auth = firebase.auth()

email = input("Syötä säpö: ")
password = input("Syötä salis: ")

user = auth.sign_in_with_email_and_password(email, password)



def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

db = firebase.database()
''' Tässä tärkeää huomata, kun on suojattu datanlähettäminen, set(data,user['idToken']) 
sallii datan lähetyksen serveriin JOS Firebasessa on annettu arvot:

{
  "rules": {
    "DHT": {
        ".read" : true,
        ".write": "'$omauidtähän' === auth.uid"
    }
  }
}

Datan siirto Firebaseen ON TEORIASSA suojattu

'''
# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").child("Morty").set(data, user['idToken'])


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

