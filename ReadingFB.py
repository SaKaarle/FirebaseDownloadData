import pyrebase
from pprint import pprint
import json

from tkinter import *
import firebase_admin
from firebase_admin import credentials
# https://www.plus2net.com/python/tkinter-OptionMenu.php
# https://stackoverflow.com/questions/50842779/optionsmenu-display-only-first-item-in-each-list
# https://pythonguides.com/python-tkinter-optionmenu/
# https://stackoverflow.com/questions/18491428/set-python-optionmenu-by-index
# pip install pyrebase4

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
        self.DateYearDay = db.child("DHT").get()

        for paiva in self.DateYearDay.each():
            self.dateTimes = paiva.val()
            self.dateTimesYear = paiva.key()
            self.vuosijapvm = []
            self.listaus = []
            #pprint(paiva.key())
            for self.klo in self.dateTimes:

                self.temp = self.dateTimes[self.klo]["Temp"]
                self.humid = self.dateTimes[self.klo]["Humid"]
                self.lampotilakatsaus = "{0} | {1} | {2}°C | {3}%"
                self.textPrint = (self.lampotilakatsaus.format(self.dateTimesYear, self.klo, self.temp, self.humid))
                self._poghamp = [self.dateTimesYear,self.klo, self.temp, self.humid]
                '''postaa ekana pvm, aika, temp ja humid '''

                self._year = [self.dateTimesYear]
                # rivi = dict(aikataulu=self.dateTimes,temperature=self.temp,kosteus=self.humid)
                # self.rivi = self._poghamp
                self.listaus.append(self.textPrint)
                self.vuosijapvm.append(self._year)
                pprint(self.textPrint)
            ### 
            #for self.infot in self.listaus:
                #pprint(self.infot)
                #print(self.poghamp)
                #print(self.dateTimes,self.temp,self.humid)
            ''' For lause printtaa vuodet'''  
            # for self.infotYear in self._year:
                # pprint([self.infotYear])
            '''Tää if-lause on rikkinäinen, mutta toimii. Pitää saada integroitua se GUI ominaisuuksiin.'''
            #self.boxText = input("Syötä lämpötila muodossa VVVV-KK-PP: ") 

# Tästä eteenpäin mars

    def GUIdisplay(self):

      def miuPainaus():
        self.myLabel = Label(self.root, text=self.textPrint)
        self.myLabel.grid(row=3,column=0)
        self.answer = self.entry1.get()
        
        if self.answer in self.dateTimesYear:
          pprint(self.listaus.append(self.textPrint))
        else:
          pprint("Syötit väärin")
        return miuPainaus
        
      self.root = Tk()
      self.root.title("Python GUI testi")
      self.root.geometry("400x300")
      #self.t = Text(self.root)
      self.entry1 = Entry(self.root, width=25,bg="darkgray")
      self.entry1.grid(row=2,column=0)
      
      dateBtn = StringVar()
      clicked1 = StringVar()
      clicked2 = StringVar()
      clicked1.set(self.vuosijapvm[0])
      clicked2.set(self.listaus[-1])      

      # drop = OptionMenu(root, clicked, self.dateTimes, self.temp, self.humid)

      dateBtn = Button(self.root,text="Syötä tiedot.",command=miuPainaus).grid(row=2,column=1)
      drop1 = OptionMenu(self.root, clicked1, *self.DateYearDay.val()).grid(row=0,column=0)
      drop2 = OptionMenu(self.root, clicked2, *self.listaus).grid(row=0,column=1)
      #drop2 = OptionMenu(root, clicked2, *[itemListaus[::] for itemListaus in self.listaus]).pack()
      
      self.root.mainloop()
if __name__ == "__main__":

    starttaus = readndisplay()
    starttaus.tappavamethodi()
    starttaus.GUIdisplay()