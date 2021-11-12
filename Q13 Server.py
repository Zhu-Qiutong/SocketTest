import socket
from time import sleep

# create and configure socket on local host
serverSocket = socket.socket()
host = socket.gethostname()
port = 65432  # arbitrary port
serverSocket.bind((host, port))
serverSocket.listen(1)

con, addr = serverSocket.accept()

print("connected to client")

while True:

    # receive wave from client
    message = con.recv(1024).decode("UTF-8")
    print(message)
    con.send(bytes(message, "UTF-8"))

    # wait 1 second
    sleep(1)