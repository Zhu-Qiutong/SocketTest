import socket
from time import sleep
import struct

# configure socket and connect to server
clientSocket = socket.socket()
host = '127.0.0.2'
port = 25000
clientSocket.connect((host, port))

while True:
    # sending massage
    user_input = input("\nPLease enter the data in turn (format: 'opcode data1 data2 ...') : ")
    opcode = int(user_input.split()[0])
    data = " ".join(user_input.split()[1:])
    info_send = struct.pack("I%ds" % (len(user_input.split()) - 1), opcode, bytes(data, "UTF-8"))
    clientSocket.sendall(info_send)

    # recive massage
    data = clientSocket.recv(1024)
    output = bytes.decode(data)
    print('server back: ', output)








