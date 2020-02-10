from PyQt5 import QtWidgets, uic
import time
import sys
app = QtWidgets.QApplication([])
win = uic.loadUi("piloto.ui") #specify the location of your .ui file
win.show()
win.txtLat.setText("asd")
win.txtLon.setText("prq")
win.txtAlertAlt.setStyleSheet("color: red;")
win.txtAlertAlt.setText("RESPUESTO ACTIVADO")
win.txtAlertGPS.setStyleSheet("color: green;")
win.txtAlertGPS.setText("OK")
i=1
#while True:
#    win.txtAlt.setText(str(i))
#    time.sleep(1)
#    i += 12
sys.exit(app.exec())
