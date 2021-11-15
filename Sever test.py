import socket
import sys
from time import sleep
import struct
import random


# create and configure socket on local host
serverSocket = socket.socket()
host = '127.0.0.2'
port = 25000  # arbitrary port
serverSocket.bind((host, port))
serverSocket.listen(1)

con, addr = serverSocket.accept()
print('conected by', addr)

while True:
    message = con.recv(1024)
    op_size = struct.calcsize("I")
    opcheck = struct.unpack("I", message[:op_size])


    if opcheck[0] == 1:
        data_size = struct.calcsize("6f")
        real_len = len(message[op_size:])

        ar = random.randint(0, 100)  # accident
        if ar < 50:
            real_len = len(message[op_size:])*2
            print("lost info")

        while real_len != data_size:
            con.send(bytes('1', "UTF-8"))
            message = con.recv(1024)
            real_len = len(message[op_size:])
            print("Retry")
            ar = random.randint(0, 100)  # accident
            if ar < 50:
                real_len = len(message[op_size:]) * 2

        data_recive = struct.unpack("6f", message[op_size:])
        con.sendall(str.encode('1, 0'))



    if opcheck[0] == 3:
        data_size = struct.calcsize("2I")
        real_len = len(message[op_size:])

        ar = random.randint(0, 100)  # accident
        if ar < 50:
            real_len = len(message[op_size:]) * 2
            print("lost info")

        while real_len != data_size:
            con.send(bytes('1', "UTF-8"))
            message = con.recv(1024)
            real_len = len(message[op_size:])
            print("Retry")
            ar = random.randint(0, 100)  # accident
            if ar < 50:
                real_len = len(message[op_size:]) * 2


        data_recive = struct.unpack("2I", message[op_size:])

        if 0 <= data_recive[0] <= 100 and 0 <= data_recive[1] <= 100:
            con.sendall(str.encode("\\3\\0"))

        else:
            con.sendall(str.encode("\\3\\1"))
