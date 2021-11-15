import socket
import sys
from time import sleep
import struct
import random


# create and configure socket on local host
serverSocket = socket.socket()
host = '127.0.0.1'
port = 25000  # arbitrary port
serverSocket.bind((host, port))
serverSocket.listen(1)

con, addr = serverSocket.accept()
print('conected by', addr)

while True:
    message = con.recv(1024)
    int_size = struct.calcsize("6s")
    # opcheck, output1 = struct.unpack("I", info_send[:int_size]), info_send[int_size:]
    opcheck = struct.unpack("6s", message[:int_size])
    opcheck = int(float(opcheck[0]))


    if opcheck == 1:
        data_size = "42s"
        data = struct.unpack(data_size, message[int_size:])
        double_check = sys.getsizeof(data)

        br = random.randint(0, 100)  # accident
        if br < 50:
            double_check = 1
            counter = 1
            while double_check != 48:
                con.send(bytes('1', "UTF-8"))
                message = con.recv(1024)
                data = struct.unpack(data_size, message[int_size:])
                double_check = sys.getsizeof(data)
                br = random.randint(0, 100)  # noise
                if br < 50:
                    double_check = 1
                print(counter)
                counter += 1

        print("pass")
        con.sendall(str.encode('1, 0'))


    elif opcheck == 3:
        data_size = "14s"
        data = struct.unpack(data_size, message[int_size:])
        double_check = sys.getsizeof(data)
        # print(double_check)
        br = random.randint(0, 100)  # noise
        if br < 50:
            double_check = 1
            counter = 1
            while double_check != 48:
                con.send(bytes('1', "UTF-8"))
                message = con.recv(1024)
                data = struct.unpack(data_size, message[int_size:])
                double_check = sys.getsizeof(data)
                br = random.randint(0, 100)  # noise
                if br < 50:
                    double_check = 1
                print(counter)
                counter += 1


        print("pass")
        message = bytes.decode(message)
        message = message.split()
        if 0 <= int(float(message[1])) <= 100 and 0 <= int(float(message[2])) <= 100:
            con.sendall(str.encode("\\3\\0"))
        else:
            con.sendall(str.encode("\\3\\1"))
