import socket
from time import sleep

ClientSocket = socket.socket()

connected = False

def connect():
   global ClientSocket
   global connected

   while not connected:
      try:
         ClientSocket.connect(("0.0.0.0", 0000)) #Select the IP and Port
         connected = True
         print("Re-connection ok")
      except socket.error:
         sleep(2)
         print("error!")

   while True:

      try:
         message = ClientSocket.recv(1024).decode("UTF-8")
         ClientSocket.send(bytes("Client side", "UTF-8"))
         print (message)
      except socket.error:
         connected = False
         ClientSocket = socket.socket()
         print("Connection Lost.. Reconnecting")
         connect()

connect()

ClientSocket.close