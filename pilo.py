import sys,time
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread 
from socketserver import ThreadingMixIn 

sock=None
wind=None

class Window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication([])
        global wind
        wind = uic.loadUi("E:\PyChram\ProyectoDistribuidasV2\piloto.ui") #specify the location of your .ui file
        
        

class ClientThread(Thread):
    def __init__(self,window): 
        Thread.__init__(self) 
        self.window=window
        
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
        self.txtAlertGPS.setStyleSheet(color)
        self.txtAlertGPS.setText(txt)

    def changeStateALT(self, alert):
        color = ''
        txt = ''
        if(alert == 1):
            color = 'color: red;'
            txt = 'RESPUESTO ACTIVADO'
        else:
            color = 'color: green;'
            txt = 'OK'
        self.txtAlertAlt.setStyleSheet(color)
        self.txtAlertAlt.setText(txt)
        
    def run(self): 
       # Variables
        HOST = 'localhost'  # Direccion IP del servidor
        PORT = 50010
        server = (HOST, PORT)
        global sock, wind
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.connect(server)
       
        while True:
            data = sock.recv(1024)
            aux = data.split('/')
            loadText(wind,aux[1],aux[2],aux[0])
            changeStateGPS(wind,aux[4])
            changeStateALT(wind,aux[3])
        sock.close() 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w=Window()
    clientThread=ClientThread(wind)
    clientThread.start()
    print(type(w))
    wind.show()
    sys.exit(app.exec_())
