from socket import *
import random
import time
import smtplib
from email.mime.text import MIMEText

# Creating a GPS devices
Flight = 'VueloNo1'

# Variables
HOST = 'localhost'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)

cord1 = [1.0,1.0]
cord2 = [1.0,1.0]
cordR = [1.0,1.0]
inc = [1.0,1.0]
mov = [1.0,1.0]
alert = 0

lat = random.random()* 180 - 90
lon = random.random()* 360 - 180
cord1[0] = lat
cord1[1] = lon
cord2 = cord1
cordR = cord1
la = 0.0
lo = 0.0
inc = [lat*0.0005, lon*0.0005]
mov = [lat*0.005, lon*0.005]

state = 1
alertado = 0

# Crear el socket
sock = socket(AF_INET, SOCK_STREAM)

#Alerta email
smtpserver = 'smtp.gmail.com:587'
login = 'torrecontrol1234@gmail.com'
password = 'Torre1234'

# Establecer coneccion
sock.connect(server)

def sender():
    global  state, alert, alertado
    message = 'GPS1: \n\tLAT: ' + str(cord1[0]) +' LON: ' + str(cord1[1]) + '\n'
    if(state == 1):
        message += 'GPS2: \n\tLAT: ' + str(cord2[0]) +' LON: ' + str(cord2[1]) + '\n'
        la = cord1[0]+cord2[0]
        lo = cord1[1]+cord2[1]
    else:
        message += 'GPS Respuesto: \n\tLAT: ' + str(cordR[0]) +'LON: ' + str(cordR[1]) + '\n' +'ERROR EN GPS2\n'
        la = cord1[0]+cordR[0]
        lo = cord1[1]+cordR[1]
    #print(message)
    msg = str(la) + '/' + str(lo) + '/' + str(alert) + '/' + message
    sock.send(msg.encode())

def validador():
    global  state, alert
    plat = (cord2[0] - cord1[0])/cord1[0]
    plon = (cord2[1] - cord1[1])/cord1[1]
    if (plat > 0.05):
        state = 0
        alert = 1
    elif (plon > 0.05):
        state = 0
        alert = 1
        alertado = 1
    if alert == 1 & alertado == 0:
        msg = MIMEText("Se activo el dispositivo  de Repuesto: Altimero")
        msg['Subject'] = "Alerta - ALT - " + Flight
        msg['From'] = 'torrecontrol1234@gmail.com'
        msg['To'] = 'inchiglemanicolax@gmail.com'
        send_email(smtpserver, login, password, msg)
        alertado[0] = 1
    #print(str(alert))


def send_email(smtpserver, login, password, msg):
    srvGoogle = smtplib.SMTP(smtpserver)
    srvGoogle.starttls()
    srvGoogle.login(login, password)
    problems = srvGoogle.sendmail(msg['From'], msg['To'], msg.as_string())
    srvGoogle.quit()


# MAIN
while True:
    if cord1[0] > 90:
        cord1[0] = -90
    elif cord1[0] < -90:
        cord1[0] = 90
    if cord1[1] > 180:
        cord1[1] = -180
    elif cord1[1] < -180:
        cord1[1] = 180
    if cord2[0] > 90:
        cord2[0] = -90
    elif cord2[0] < -90:
        cord2[0] = 90
    if cord2[1] > 180:
        cord2[1] = -180
    elif cord2[1] < -180:
        cord2[1] = 180
    if cordR[0] > 90:
        cordR[0] = -90
    elif cordR[0] < -90:
        cordR[0] = 90
    if cordR[1] > 180:
        cordR[1] = -180
    elif cordR[1] < -180:
        cordR[1] = 180

    cord1[0] += mov[0]
    cord2[0] += mov[0]+inc[0]
    cordR[0] += mov[0]
    cord1[1] += mov[1]
    cord2[1] += mov[1]+inc[1]
    cordR[1] += mov[1]
    validador()
    sender()
    time.sleep(0.2)


# Cerrar coneccion
sock.close()
