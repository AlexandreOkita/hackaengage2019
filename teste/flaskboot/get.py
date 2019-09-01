import pyrebase

config = {
  "apiKey": "AIzaSyDbTLSOPNwsnCjm3rgYOqVGNt-uQLPK6EM",
  "authDomain": "malltup-hackengage.firebaseapp.com",
  "databaseURL": "https://malltup-hackengage.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def get_info():
    feed = db.child('Eventos').get().val()
    lista = []
    for i in feed:
        evento = []
        evento.append(db.child('Eventos').child(i).child('Titulo').get().val())
        evento.append(db.child('Eventos').child(i).child('Descricao').get().val())
        evento.append(db.child('Eventos').child(i).child('Local').get().val())
        evento.append(db.child('Eventos').child(i).child('Data').get().val())
        lista.append(evento)
    lista_invertida = []
    for i in range(len(lista)):
        lista_invertida.append(lista[-i-1])
    return lista_invertida
