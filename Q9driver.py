#!/usr/bin/env python3

import socket
import struct

# setup
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
#initialization
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
#loop
    while True:

        #sending massage
        massage_send = bytes(input("\nPLease enter the data in turn (format: 'opcode data1 data2 ...') : "), 'utf-8')
        data = struct.pack("I%ds" % (len(massage_send),), len(massage_send), massage_send)
        s.sendall(data)

        #recive massage
        data = s.recv(1024)
        output = bytes.decode(data)
        print('server back: ', output)