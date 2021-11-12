#!/usr/bin/env python3

import socket
import pickle
# setup
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


#initialization
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
#loop
    while True:

        #sending massage
        # n = float(input("\nPLease enter OP code : "))
        #
        # if n == 1:
        #     n = 6
        # elif n == 2:
        #     n = 7
        # elif n == 3:
        #     n = 2
        #
        #     # Below line read inputs from user using map() function
        # massage_send = list(map(float, input("\nPLease enter the data in turn (format: '0 0 0 ...'): ").strip().split()))[:n]
        # data_send = pickle.dumps(massage_send)
        # s.send(data_send)
        massage_send = list(map(float, input("\nPLease enter the data in turn (format: 'opcode data'): ").strip().split()))
        data_send = pickle.dumps(massage_send)
        s.send(data_send)

        # massage_send = str(massage_send)
        # massage_send = massage_send.encode
        # s.send(massage_send)

        #recive massage
        data = s.recv(1024)
        # data = pickle.loads(data)
        # data = data.decode('utf-8','strict')
        # output = data.decode('UTF-8','strict')
        # print('server back:', 'ACK' + output)
        # data = str(data, 'utf-8')
        data = bytes.decode(data)
        print('\nServer back: ', data)
        # str = '[0, 0]'
        # str_utf8 = str.encode("UTF-8")
        # print(str_utf8)

