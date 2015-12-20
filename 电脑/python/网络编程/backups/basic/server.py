#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:break
    conn.sendall(data)
conn.close()

#if __name__ == '__main__':
