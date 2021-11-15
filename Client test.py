import socket
from time import sleep
import struct


# configure socket and connect to server
clientSocket = socket.socket()
host = '127.0.0.2'
port = 25000
clientSocket.connect((host, port))
data_send = 0

while True:

    user_input = input("\nPLease enter the data in turn (format: 'opcode data1 data2 ...') : ")
    user_input = user_input.split()
    opcode = int(user_input[0])
    if opcode == 1:
        data = list(map(float, user_input[1:]))
        data_send = struct.pack("I6f", opcode, *(i for i in data))
        clientSocket.sendall(data_send)

    elif opcode == 3:
        data = list(map(int, user_input[1:]))
        data_send = struct.pack("3I", opcode, *(i for i in data))
        clientSocket.sendall(data_send)




    # recive massage
    data_recive = clientSocket.recv(1024).decode("UTF-8")
    try:
        check = int(data_recive)
        while check == 1:
            # print(check)
            clientSocket.sendall(data_send)
            data_recive = clientSocket.recv(1024).decode("UTF-8")
            check = int(data_recive)
            print("Trying to resend...")
            sleep(1)
        print("Resend succeed!")

    except ValueError:
        print('Server back: ', data_recive)

