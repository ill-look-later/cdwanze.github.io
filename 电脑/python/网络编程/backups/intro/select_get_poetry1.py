#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime, argparse, socket

import selectors
sel = selectors.DefaultSelector()

def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, blocking edition.
Run it like this:

  python3 select_get_poetry3.py port1 port2 port3 ...

通过select I/O复用来建立一个异步诗歌下载客户端，可以同时面向多个诗歌服务器来进行下载。
"""

    parser = argparse.ArgumentParser(usage)
    parser.add_argument('port',nargs='+')

    args = vars(parser.parse_args())
    addresses = args['port']

    if not addresses:
        print(parser.format_help())
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)

def download_poetry(sock,infile):
    """Download a piece of poetry from the given address."""

    bstring = sock.recv(1024)

    if not bstring:###end fo reading
        sel.unregister(sock)
        infile.close()
        print('end of reading')
        return True
    else:
        print('writing to {}'.format(infile.name))
        infile.write(bstring)


def connect(address):
    """Connect to the given server and return a non-blocking socket."""
    sock = socket.socket()
    sock.connect(address)
    sock.setblocking(False)
    return sock

def format_address(address):
    host, port = address
    return '%s:%s' % (host or '127.0.0.1', port)

def main():
    addresses = parse_args()
    elapsed = datetime.timedelta()
    sockets = map(connect, addresses)

    for sock in sockets:
        filename = str(sock.getpeername()[1]) + '.txt'
        infile = open(filename,'wb')
        sel.register(sock, selectors.EVENT_READ,
        data={'callback':download_poetry,
        'args':[infile]})

    while True:
        events = sel.select()
        for key,mask in events:
            callback = key.data['callback']
            callback(key.fileobj, *key.data['args'])



if __name__ == '__main__':
    main()
