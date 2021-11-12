#!/usr/bin/env python3

import socket
import time
import struct

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            output1 = conn.recv(1024)

            if not output1:
                break

            int_size = struct.calcsize("I")
            (i,), output1 = struct.unpack("I", output1[:int_size]), output1[int_size:]
            output1 = bytes.decode(output1)
            output1 = output1.split()
            opcheck = int(output1[0])

            if opcheck == 1:
                time.sleep(0.5)
                conn.sendall(str.encode('1 0'))

            if opcheck == 3:
                if 0 <= int(output1[1]) <= 100 and 0 <= int(output1[2]) <= 100:
                    conn.sendall(str.encode("\\3\\0"))
                else:
                    conn.sendall(str.encode("\\3\\1"))