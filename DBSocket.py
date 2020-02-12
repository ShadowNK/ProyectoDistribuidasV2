from socket import *
import datetime
from firebase.firebase import FirebaseApplication, FirebaseAuthentication



# Variables
HOST = 'localhost'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)




# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

# Firebase
SECRET = '942534492089'
EMAIL = 'inchiglemanicolax@gmail.com'
DSN = 'https://distribuidase3.firebaseio.com/'
BDname = '/distribuidase3/' + Flight
auth = FirebaseAuthentication(SECRET, EMAIL, True, True)
firebase = FirebaseApplication(DSN, None)

gpsData = { 'lat': '',
            'lon': '',
            'GPSW': '',
            'date': datetime.datetime.now()}
altData = { 'alt': '',
            'ALTW': '',
            'date': datetime.datetime.now()}

# Establecer coneccion
sock.connect(server)

def reciver():
    reply = sock.recv(1024)
    print(reply.decode())
    aux = reply.decode().split('/')
    writter(reply.decode())


def writter(data):
    if(len(data) != 0):
        aux = data.split('/')
        if(aux[0]=='GPS'):
            writterGPS(aux[1], aux[2], aux[3])
        else:
            writterALT(aux[1], aux[2])

def writterGPS(lat, lon, alert):
    global alertado
    gpsData = { 'lat': lat,
            'lon': lon,
            'GPSW': alert,
            'date': datetime.datetime.now()}
    snapshot = firebase.post(BDname+'-GPS', gpsData)
    print(snapshot['name'])


def writterALT(alt, alert):
    global alertado
    altData = { 'alt': alt,
            'ALTW': alert,
            'date': datetime.datetime.now()}
    snapshot = firebase.post(BDname+'-ALT', altData)
    print(snapshot['name'])

    
# MAIN
while True:
    reciver()

# Cerrar coneccion
sock.close()
