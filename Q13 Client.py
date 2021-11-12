import socket
from time import sleep

# configure socket and connect to server
clientSocket = socket.socket()
host = socket.gethostname()
port = 65432
clientSocket.connect((host, port))

# keep track of connection status
connected = True
print("connected to server")

while True:
    # attempt to send and receive wave, otherwise reconnect
    try:
        user_input = input('Please type something: ')
        if user_input == 'exit':
            print('Test Finished!')
            break
        clientSocket.send(bytes(user_input, "UTF-8"))
        message = clientSocket.recv(1024).decode("UTF-8")
        print('server back:', message)

    except socket.error:
        # set connection status and recreate socket
        connected = False
        clientSocket = socket.socket()
        print("connection lost... reconnecting")
        while not connected:
            # attempt to reconnect, otherwise sleep for 2 seconds
            try:
                clientSocket.connect((host, port))
                connected = True
                print("re-connection successful")
            except socket.error:
                sleep(2)