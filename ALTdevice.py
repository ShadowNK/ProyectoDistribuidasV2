from socket import *
import random
import time
import smtplib
from email.mime.text import MIMEText

# Creating a ALT devices
Flight = 'VueloNo1'

# Variables
HOST = 'localhost'  # Direccion IP del servidor
PORT = 50010
server = (HOST, PORT)

alt1 = 1
alt2 = 1
altR = 1
inc = 0
mov = 0
alert = 0

alt1 = random.random() * 3200
alt2 = alt1
altR = alt1
inc = alt1*0.00003
mov = alt1*0.0005

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
    global  state, alert
    message = 'ALT1: ' + str(alt1) + '\n'
    if(state == 1):
        message += 'ALT2: ' + str(alt2) + '\n'
        msg = str(alt1+alt2) + '/' + str(alert) + '/' + message
    else:
        message += 'ALT Respuesto: ' + str(altR) + '\n' +'ERROR EN ALT2\n'
        msg = str(alt1+altR) + '/' + str(alert) + '/' + message
    #print(message)
    sock.send(msg.encode())

def validador():
    global  state, alert, alertado
    palt = (alt2 - alt1)/alt1
    if (palt > 0.05):
        state = 0
        alert = 1
        alertado = 1
    if alert == 1 & alertado == 0:
        msg = MIMEText("Se activo el dispositivo  de Repuesto: GPS")
        msg['Subject'] = "Alerta - GPS - " + Flight
        msg['From'] = 'torrecontrol1234@gmail.com'
        msg['To'] = 'inchiglemanicolax@gmail.com'
        send_email(smtpserver, login, password, msg)
        alertado[1] = 1
    #print(str(alert))


def send_email(smtpserver, login, password, msg):
    srvGoogle = smtplib.SMTP(smtpserver)
    srvGoogle.starttls()
    srvGoogle.login(login, password)
    problems = srvGoogle.sendmail(msg['From'], msg['To'], msg.as_string())
    srvGoogle.quit()


# MAIN
while True:
    alt1 += mov
    alt2 += mov+inc
    altR += mov
    validador()
    sender()
    time.sleep(0.11)
    

# Cerrar coneccion
sock.close()
