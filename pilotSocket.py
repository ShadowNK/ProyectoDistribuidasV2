# GUI LIBRARIES
import sys
from socket import *
from PyQt5 import *
from _thread import *

# Functions for UI
class window(QDialog):
    def __init__(self):
        super().__init__()
        # Run window
        app = QtWidgets.QApplication([])
        win = uic.loadUi("piloto.ui") #specify the location of your .ui file
        win.show()
        
    def loadText(self, lat, lon, alt):
        self.txtLat.setText(lat)
        self.txtLon.setText(lon)
        self.txtAlt.setText(alt)

    def changeStateGPS(self, alert):
        color = ''
        txt = ''
        if(alert == 1):
            color = 'color: red;'
            txt = 'RESPUESTO ACTIVADO'
        else:
            color = 'color: green;'
            txt = 'OK'
        win.txtAlertGPS.setStyleSheet(color)
        win.txtAlertGPS.setText(txt)

    def changeStateALT(self, alert):
        color = ''
        txt = ''
        if(alert == 1):
            color = 'color: red;'
            txt = 'RESPUESTO ACTIVADO'
        else:
            color = 'color: green;'
            txt = 'OK'
        win.txtAlertAlt.setStyleSheet(color)
        win.txtAlertAlt.setText(txt)
        
# Creating a socket
class sock(Thread):
    
    # Variables
    HOST = 'localhost'  # Direccion IP del servidor
    PORT = 50010
    server = (HOST, PORT)
    sock = socket(AF_INET, SOCK_STREAM)
    
    def __init__(self):
        super().__init__()
        sock.connect(server)

    def reciver():
        while True:
            reply = sock.recv(1024)
            aux = reply.decode().split('/')
            loadText(win, aux[1], aux[2], aux[0])
            changeStateALT(win, aux[3])
            changeStateGPS(win, aux[4])
        sock.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = window()
    sock(win)
    win.exec()

    
### Comunicacion
##start_new_thread(reciver,())
##
### Cerrar coneccion
##sys.exit(app.exec())

#https://github.com/anuranBarman/Python-Chat-Application-Using-PyQt-and-Socket/blob/master/server.py
