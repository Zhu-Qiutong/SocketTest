#!/usr/bin/env python3

import socket
# setup
HOST = '127.0.0.2'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
#initialization
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
#loop
    while True:

        #sending massage
        user_input = input('Please type something: ')
        if user_input == 'exit':
            print('Test Finished!')
            break
        massage_send = str.encode(user_input)
        s.sendall(massage_send)

        #recive massage
        data = s.recv(1024)
        output = bytes.decode(data)
        print('server back:', 'ACK' + output)


