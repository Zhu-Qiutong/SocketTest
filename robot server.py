#!/usr/bin/env python3

import socket
import pickle
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data = pickle.loads(data)

            if not data:
                break

            # Opcode 1
            if data[0] == 1:
                if len(data[1:]) == 6:
                    time.sleep(0.5)
                    conn.sendall(str.encode('1 OK'))
                else:
                    conn.sendall(str.encode('0 NG'))

            # Opcode 2
            if data[0] == 2:
                if len(data[1:]) == 7:
                    time.sleep(1)
                    conn.sendall(str.encode('2 OK'))
                else:
                    conn.sendall(str.encode('0 NG'))

            # Opcode 3
            if data[0] == 3:
                if len(data[1:]) == 2:
                    if 0 <= data[1] <= 100 and 0 <= data[2] <= 100:
                        conn.sendall(str.encode('3 OK'))
                    else:
                        conn.sendall(str.encode('3 NG'))
                else:
                    conn.sendall(str.encode('0 NG'))