from socket import *
from _thread import *
import datetime
import time

HOST = 'localhost'  # Direccion IP del seridor
PORT = 50010
bd = (socket(),'')
pilot = (socket(),'')
send = 0
data = [0, 0, 0, 0, 0]
AltCon = 0
GPSCon = 0

# VARIABLES ALT
server = (HOST, PORT)

# SOCKET ALT
sock = socket()                 # Create a socket object
sock.bind(server)               # Bind to the port
sock.listen(5)                  # Number of connections


## Devices Altitud

def on_new_alt(clientsocket,addr):
    global data, AltCon
    print ("Conectado con ALT: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        if send == 1:
            aux = msg.decode().split('/')
            data[0] += float(aux[0])
            data[3] = float(aux[1])
            AltCon += 2
            ms = 'ALT/' + str(data[0]) + '/' + str(data[3]) + '/' + str(data[4])
            resend_to_BD(ms.encode())

    clientsocket.close()


## Devices GPS

def on_new_gps(clientsocket,addr):
    global data, GPSCon
    print ("Conectado con GPS: ", addr)
    while True:
        msg = clientsocket.recv(1024)
        if send == 1:
            aux = msg.decode().split('/')
            data[1] += float(aux[0])
            data[2] += float(aux[1])
            data[4] = float(aux[2])
            GPSCon += 2
            ms = 'GPS/' + str(data[1]) + '/' + str(data[2]) + '/' + str(data[4])
            resend_to_BD(ms.encode())
    clientsocket.close()


## DB device

def on_new_BD(clientsocket,addr):
    print ("Conectado con BD: ", addr)
    global bd, send
    #send = 1
    bd = (clientsocket, addr)

def resend_to_BD(ms):
    (clientsocket,addr) = bd
    #print(ms.decode())
    clientsocket.send(ms)


## PILOT device
            
def on_new_p(clientsocket,addr):
    print ("Conectado con Pilot: ", addr)
    global pilot, send
    pilot = (clientsocket,addr)
    send = 1
    while True:
        pilot_calc()

def pilot_calc():
    global data, AltCon, GPSCon
    if(AltCon >= 40 | GPSCon >= 20):
        al = data[0]/AltCon
        la = data[1]/GPSCon
        lo = data[2]/GPSCon
        aa = data[3]
        ag = data[4]
        resend_to_p(al, la, lo, aa, ag)
        data = [0, 0, 0, aa, ag]
        AltCon = 0
        GPSCon = 0

def resend_to_p(al, la, lo, aa, ag):
    (clientsocket,addr) = pilot
    msg = str(al) + '/' + str(la) + '/' + str(lo) + '/' + str(aa) + '/' + str(ag)
    print(msg)
    clientsocket.send(msg.encode())



input("Conectar el altimetro...")
conn, addr = sock.accept()
start_new_thread(on_new_alt,(conn,addr))
time.sleep(0.1)

input("Conectar el gps...")
conn, addr = sock.accept()
start_new_thread(on_new_gps,(conn,addr))
time.sleep(0.1)

input("Conectar la bd...")
conn, addr = sock.accept()
start_new_thread(on_new_BD,(conn,addr))
time.sleep(0.1)

input("Conectar el piloto...")
conn, addr = sock.accept()
start_new_thread(on_new_p,(conn,addr))
time.sleep(0.1)


input("press enter to finish")

sock.close()
