import pyrebase

config = {
  "apiKey": "AIzaSyDbTLSOPNwsnCjm3rgYOqVGNt-uQLPK6EM",
  "authDomain": "malltup-hackengage.firebaseapp.com",
  "databaseURL": "https://malltup-hackengage.firebaseio.com",
  "storageBucket": "projectId.appspot.com"

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
db.child("arqueiros").push(archer)
users = db.child("arqueiros").get()
print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}