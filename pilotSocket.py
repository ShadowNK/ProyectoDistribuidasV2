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
        self.lblLat.setText()

    def changeStateGPS(self):
        self.lblAlertGPS.setColor();

    def changeStateALT(self):
        self.lblAlertAlt.setColor();


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
    widget.loadText(widget, aux[1], aux[2], aux[0])


# Comunicacion
while True:
    reciver()

# Cerrar coneccion
sock.close()
sys.exit(app.exec_())
