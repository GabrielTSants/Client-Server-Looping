import socket
from time import sleep

def server():
   serverSocket = socket.socket()
   serverSocket.bind(("0.0.0.0", 0000)) #Select the IP and Port
   serverSocket.listen(1)
   con, addr = serverSocket.accept()
   print( "connected to client" )


   while True:
      try:
         con.send(bytes("Server side", "UTF-8"))
         message = con.recv(1024).decode("UTF-8")
         print(message)
         sleep(1)
      except socket.error:
         serverSocket = socket.socket
         print("Lost Connection, reconnecting!")
         server()

   con.close();







server()