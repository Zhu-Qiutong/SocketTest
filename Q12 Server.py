import socket
from time import sleep

# create and configure socket on local host  
serverSocket = socket.socket()
host = socket.gethostname()
port = 25000  # arbitrary port
serverSocket.bind((host, port))
serverSocket.listen(1)

con, addr = serverSocket.accept()
connected = True
print('Connected by', addr)


while True:

    try:
        # send wave to client
        # con.send(bytes("Server wave", "UTF-8"))
        # receive wave from client
        message = con.recv(1024).decode("UTF-8")
        print(message)
        # print(type(message))
        send_back = "ACK" + message
        # print(send_back)
        # print(type(send_back))
        con.send(bytes(send_back, "UTF-8"))

        # wait 1 second
        sleep(1)
    except socket.error:
        # set connection status and recreate socket
        connected = False
        # clientSocket = socket.socket()
        print("connection lost... reconnecting")
        while not connected:
            # attempt to reconnect, otherwise sleep for 2 seconds
            try:
                con, addr = serverSocket.accept()
                connected = True
                print("re-connection successful")
            except socket.error:
                sleep(2)