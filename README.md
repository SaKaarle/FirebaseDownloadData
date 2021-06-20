### FirebaseDownloadData

Firebase database vain readonlynä ja write dataa pystyy vaan annetulla UID:llä databaseen (Firebasen Realtime Database)

{
  
  "rules": {
    
    "DHT": {
      
        ".read" : true,
          
        ".write": "'your.uid.hereasdasdasdasdas' === auth.uid"
          
    }
      
  }
    
}
  


### imports
`import pyrebase`
  
`from pprint import pprint`
  
`import json`
  
`from tkinter import *`
  
`import firebase_admin`
  
`from firebase_admin import credentials`
  
