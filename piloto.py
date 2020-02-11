# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyChram\ProyectoDistribuidasV2\piloto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from threading import Thread

sock = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblGPS = QtWidgets.QLabel(self.centralwidget)
        self.lblGPS.setGeometry(QtCore.QRect(40, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblGPS.setFont(font)
        self.lblGPS.setObjectName("lblGPS")
        self.lblLat = QtWidgets.QLabel(self.centralwidget)
        self.lblLat.setGeometry(QtCore.QRect(120, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblLat.setFont(font)
        self.lblLat.setObjectName("lblLat")
        self.lblLon = QtWidgets.QLabel(self.centralwidget)
        self.lblLon.setGeometry(QtCore.QRect(120, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblLon.setFont(font)
        self.lblLon.setObjectName("lblLon")
        self.lblAlertGPS = QtWidgets.QLabel(self.centralwidget)
        self.lblAlertGPS.setGeometry(QtCore.QRect(540, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblAlertGPS.setFont(font)
        self.lblAlertGPS.setObjectName("lblAlertGPS")
        self.lblAltimetro = QtWidgets.QLabel(self.centralwidget)
        self.lblAltimetro.setGeometry(QtCore.QRect(40, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblAltimetro.setFont(font)
        self.lblAltimetro.setObjectName("lblAltimetro")
        self.lblAlertAlt = QtWidgets.QLabel(self.centralwidget)
        self.lblAlertAlt.setGeometry(QtCore.QRect(510, 190, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblAlertAlt.setFont(font)
        self.lblAlertAlt.setObjectName("lblAlertAlt")
        self.lblAlt = QtWidgets.QLabel(self.centralwidget)
        self.lblAlt.setGeometry(QtCore.QRect(120, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblAlt.setFont(font)
        self.lblAlt.setObjectName("lblAlt")
        self.txtLat = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLat.setGeometry(QtCore.QRect(220, 70, 191, 20))
        self.txtLat.setReadOnly(True)
        self.txtLat.setObjectName("txtLat")
        self.txtAlt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlt.setGeometry(QtCore.QRect(220, 240, 191, 20))
        self.txtAlt.setReadOnly(True)
        self.txtAlt.setObjectName("txtAlt")
        self.txtLon = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLon.setGeometry(QtCore.QRect(220, 110, 191, 20))
        self.txtLon.setReadOnly(True)
        self.txtLon.setObjectName("txtLon")
        self.txtAlertAlt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlertAlt.setGeometry(QtCore.QRect(540, 240, 131, 20))
        self.txtAlertAlt.setReadOnly(True)
        self.txtAlertAlt.setObjectName("txtAlertAlt")
        self.txtAlertGPS = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlertGPS.setGeometry(QtCore.QRect(540, 70, 131, 20))
        self.txtAlertGPS.setMouseTracking(False)
        self.txtAlertGPS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtAlertGPS.setReadOnly(True)
        self.txtAlertGPS.setObjectName("txtAlertGPS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblGPS.setText(_translate("MainWindow", "GPS"))
        self.lblLat.setText(_translate("MainWindow", "Latitud:"))
        self.lblLon.setText(_translate("MainWindow", "Longitud:"))
        self.lblAlertGPS.setText(_translate("MainWindow", "ESTADO GPS"))
        self.lblAltimetro.setText(_translate("MainWindow", "ALTIMETRO"))
        self.lblAlertAlt.setText(_translate("MainWindow", "ESTADO ALTIMETRO"))
        self.lblAlt.setText(_translate("MainWindow", "Altitud:"))

    def loadText(self, lat, lon, alt):
        self.txtLat.setText(lat)
        self.txtLon.setText(lon)
        self.txtAlt.setText(alt)

    def changeStateGPS(self, alert):
        color = ''
        txt = ''
        if (alert == 1):
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
        if (alert == 1):
            color = 'color: red;'
            txt = 'RESPUESTO ACTIVADO'
        else:
            color = 'color: green;'
            txt = 'OK'
        self.txtAlertAlt.setStyleSheet(color)
        self.txtAlertAlt.setText(txt)


class ClientThread(Thread):

    window = None

    def __init__(self, Window):
        global window
        Thread.__init__(self)
        window = Window

    def run(self):
        HOST = 'localhost'  # Direccion IP del servidor
        PORT = 50010
        server = (HOST, PORT)
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server)
        while True:
            data = sock.recv(1024)
            aux = data.decode().split('/')
            Ui_MainWindow.loadText(window, aux[1], aux[2], aux[0])
            Ui_MainWindow.changeStateALT(window, aux[3])
            Ui_MainWindow.changeStateGPS(window, aux[4])
        sock.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    clientThread = ClientThread(ui)
    clientThread.start()
    MainWindow.show()
    sys.exit(app.exec_())
