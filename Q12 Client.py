import socket
from time import sleep

# configure socket and connect to server
clientSocket = socket.socket()
host = socket.gethostname()
port = 25000
clientSocket.connect((host, port))

# keep track of connection status
connected = True
print("connected to server")

while True:
    # attempt to send and receive wave, otherwise reconnect
        clientSocket.send(bytes("Client wave", "UTF-8"))
        message = clientSocket.recv(1024).decode("UTF-8")
        print(message)

