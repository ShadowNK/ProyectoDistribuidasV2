# GUI LIBRARIES
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWindgets import QApplication, QDialog
from PyQt5.uic import loadUi
from socket import *


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('piloto.ui', self)

    def loadText(self, lat, lon, alt):
        self.txtLat.setText(lat)
        self.txtLon.setText(lon)
        self.txtAlt.setText(alt)

    def changeStateGPS(self, alert):
        color =''
        if(alert == 1):
            color = '0000000'
        else:
            color = 'FFFFFF'
        self.txtAlertGPS.setColor(color)

    def changeStateALT(self, alert):
        color =''
        if(alert == 1):
            color = '0000000'
        else:
            color = 'FFFFFF'
        self.txtAlertAlt.setColor(color)


# Creating a clientsocket

# Variables
HOST = '172.31.108.23'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)

# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()

# Establecer coneccion
sock.connect(server)

def reciver():
    reply = sock.recv(1024)
    aux = reply.decode().split('/')
    widget.loadText(aux[1], aux[2], aux[0])
    widget.changeStateALT(aux[3])
    widget.changeStateGPS(aux[4])

# Comunicacion
while True:
    reciver()

# Cerrar coneccion
sock.close()
sys.exit(app.exec_())
