import pyrebase
from pprint import pprint
import json

from tkinter import *
import firebase_admin
from firebase_admin import credentials
### https://www.plus2net.com/python/tkinter-OptionMenu.php
### https://stackoverflow.com/questions/50842779/optionsmenu-display-only-first-item-in-each-list
### https://pythonguides.com/python-tkinter-optionmenu/
### pip install pyrebase4

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

cred = credentials.Certificate(
    'F:/code/Firebase/temperatureproject-666-firebase-admin.json')
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


class readndisplay:

  def tappavamethodi(self):
      DateYearDay = db.child("DHT").get()

      for paiva in DateYearDay.each():
          self.datetimes = paiva.val()
          self.dateTimesYear = paiva.key()
          self.vuosijapvm = []
          self.listaus = []
          for klo in self.datetimes:

              self.temp = self.datetimes[klo]["Temp"]
              self.humid = self.datetimes[klo]["Humid"]
              self.lampotilakatsaus = "{0} | {1} | {2}°C | {3}%"
              #self._poghamp = [(self.lampotilakatsaus.format(self.dateTimesYear, klo, self.temp, self.humid))]
              self._poghamp = [self.dateTimesYear, klo, self.temp, self.humid]
              self._year = [self.dateTimesYear]
              # rivi = dict(aikataulu=self.datetimes,temperature=self.temp,kosteus=self.humid)
              #self.rivi = self._poghamp
              self.listaus.append(self._poghamp)
              self.vuosijapvm.append(self._year)
          for infot in self.listaus:
            pprint([infot])
              # print(self.poghamp)
              # print(self.datetimes,self.temp,self.humid)
          for infotYear in self._year:
            pprint([infotYear])

# Tästä eteenpäin mars

  def GUIpaska(self):
      root = Tk()
      root.title("Python GUI testi")
      root.geometry("400x200")

      clicked1 = StringVar()
      clicked2 = StringVar()
      clicked1.set(self.vuosijapvm[0])
      clicked2.set(self.listaus[0])
      # drop = OptionMenu(root, clicked, self.datetimes, self.temp, self.humid)
      
      drop1 = OptionMenu(root, clicked1, *self.vuosijapvm).pack(expand=True)
      drop2 = OptionMenu(root, clicked2, *self.listaus).pack(expand=True)
      #drop2 = OptionMenu(root, clicked2, *[itemListaus[::] for itemListaus in self.listaus]).pack()

      root.mainloop()


if __name__ == "__main__":

  starttaus = readndisplay()
  starttaus.tappavamethodi()
  starttaus.GUIpaska()