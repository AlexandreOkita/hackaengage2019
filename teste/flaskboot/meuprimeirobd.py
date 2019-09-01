import pyrebase

config = {
  "apiKey": "AIzaSyDbTLSOPNwsnCjm3rgYOqVGNt-uQLPK6EM",
  "authDomain": "malltup-hackengage.firebaseapp.com",
  "databaseURL": "https://malltup-hackengage.firebaseio.com",
  "storageBucket": "projectId.appspot.com"

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def set_info(titulo, desc, local, data):
  evento1 = {"Titulo": titulo, "Descricao": desc, "Local": local, "Data": data}
  db.child("Eventos").push(evento1)

def get_info():
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()
  return [db.child('Eventos').child('data').get().val()]
