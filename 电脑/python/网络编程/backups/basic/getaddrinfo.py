#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
socket.setdefaulttimeout(10)


addrinfos = socket.getaddrinfo('www.python.org','https')

for addrinfo in addrinfos:
    socket_parameter = addrinfo[:3]
    print(socket_parameter)
    addr = addrinfo[-1]
    print(addr)

    s = socket.socket(*socket_parameter)
    try:
        s.connect(addr)
        print('connected')
        print('peername',s.getpeername())
        print('hostname',s.getsockname())
    #except socket.timeout:
        #print('socket timeout')
    except Exception as e:
        print(e)



#if __name__ == '__main__':
