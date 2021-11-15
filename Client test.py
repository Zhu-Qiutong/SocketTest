import socket
from time import sleep
import struct


def padding(c):
    c = "{:.2f}".format(c)
    c = c.zfill(6)
    return c


# configure socket and connect to server
clientSocket = socket.socket()
host = '127.0.0.1'
port = 25000
clientSocket.connect((host, port))

while True:
    user_input = input("\nPLease enter the data in turn (format: 'opcode data1 data2 ...') : ")
    data = user_input.split()
    data = list(map(float, data))
    data = [padding(c) for c in data]
    data = " ".join(data)
    info_send = struct.pack("%ds" % len(data), bytes(data, "UTF-8"))
    clientSocket.sendall(info_send)


    # recive massage
    data_recive = clientSocket.recv(1024).decode("UTF-8")
    try:
        check = int(data_recive)
        while check == 1:
            # print(check)
            clientSocket.sendall(info_send)
            data_recive = clientSocket.recv(1024).decode("UTF-8")
            check = int(data_recive)
            print("Trying to resend...")
            sleep(1)
        print("Resend succeed!")

    except ValueError:
        print('Server back: ', data_recive)

