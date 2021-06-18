import pyrebase
from pprint import pprint

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
#auth = firebase.auth()
def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

db = firebase.database()

# dataJuuri = db.child("DHT").shallow().get()
# osaDataa = db.child("DHT/").get()
# for dataJuuri in osaDataa.each():
#       LmpData = db.child("DHT/").order_by_child("2020-03-31").limit_to_first(1).get()

# rapsYear = db.child().get() #TOI YKS HAKEE DATAN
# testi Temp = db.child("Raspi").order_by_child("Temp").limit_to_first(1).get()

# raspKlo= db.child("Raspi/2020-03-29").get()
# Temp = db.child().get()
# print(rapsYear.val())

# Avainmen syönti jos sellainen on:

# pvmkey = db.child().get()
# print(pvmkey.key())


# EITOIMI
# dhtData = db.child("Raspi/").get()

# inventorydb = db.child("Raspi/")
# for dhtid in inventorydb.shallow().get().each():
#     productdb = dhtData.child(dhtid)
#     # print the ids
#     print([id for id in productdb.shallow().get()])

# RaspiData = db.child("Raspi/")
# for rapsDHT in RaspiData.shallow().get().each():

#     dhtData = db.key()
#     temphumd = db.child("pvm").child(dhtData).get()

#     print([id for id in dhtData.shallow().get()])
#jotenkuten ei toimi tää ei 
# osaDataa = db.child('Raspi').order_by_key("Temp").get(json_kwargs={1})
# for dataJuuri in osaDataa.each():
#     print(dataJuuri.key())
# osumaData = db.get(osaDataa['2020-03-31'])

#tää toimii älä muuta, kopypastee tätä
#Toimiva luku
osaDataa = db.child("DHT/").get()
for dataJuuri in osaDataa.each():
    print(dataJuuri.key())
    print(dataJuuri.val())
    # for raspKlo in raspDHT.each():
    #     print(raspKlo.key())
    #     print(raspKlo.val())
    #     for Temp in raspKlo.each():
    #         print(Temp.key())