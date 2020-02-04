from socket import *
import datetime
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

# Creating a clientsocket

# Variables
HOST = '172.31.108.23'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)

# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

# Firebase
SECRET = '942534492089'
EMAIL = 'inchiglemanicolax@gmail.com'
DSN = 'https://distribuidase3.firebaseio.com/'
BDname = '/vuelo1'
auth = FirebaseAuthentication(SECRET, EMAIL, True, True)
firebase = FirebaseApplication(DSN, auth)

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
    writter(reply.decode())

def writter(data):
    if(len(data) != 0):
        aux = data.split('/')
        if(aux[0]=='GPS'):
            writterGPS(aux[1], aux[2], aux[3])
        else:
            writterALT(aux[1], aux[2])

def writterGPS(lat, lon, alert):
    gpsData = { 'lat': lat,
            'lon': lon,
            'GPSW': alert,
            'date': datetime.datetime.now()}
    snapshot = firebase.post(BDname, gpsData)
    print(snapshot['name'])


def writterALT(alt, alert):
    altData = { 'alt': alt,
            'ALTW': alert,
            'date': datetime.datetime.now()}
    snapshot = firebase.post(BDname, altData)
    print(snapshot['name'])

    
# MAIN
while True:
    reciver()

# Cerrar coneccion
sock.close()
