import socket
from time import sleep
import struct


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
    int_size = struct.calcsize("I")
    # opcheck, output1 = struct.unpack("I", info_send[:int_size]), info_send[int_size:]
    opcheck = struct.unpack("I", message[:int_size])
    opcheck = int(opcheck[0])

    #
    if opcheck == 1:
        data_size = 6
        # con.sendall(str.encode('1'))

        message = con.recv(1024)







    elif opcheck == 2:
        data_size = 1
        con.sendall(str.encode('2'))
    print(data_size)
    # output1 = bytes.decode(output1)
    # output1 = output1.split()
    # opcheck = int(output1[0])

    # if opcheck == 1:
    #     sleep(0.5)
    #     con.sendall(str.encode('1, 0'))
    #
    # if opcheck == 3:
    #     if 0 <= int(output1[1]) <= 100 and 0 <= int(output1[2]) <= 100:
    #         con.sendall(str.encode("\\3\\0"))
    #     else:
    #         con.sendall(str.encode("\\3\\1"))


