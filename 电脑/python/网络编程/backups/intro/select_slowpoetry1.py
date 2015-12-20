#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, socket, time
import selectors

sel = selectors.DefaultSelector()

def parse_args():
    usage = """usage: %prog [options] poetry-file

This is the Slow Poetry Server, blocking edition.
Run it like this:

  python3 select_slowpoetry3.py ecstasy.txt

"""

    parser = argparse.ArgumentParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_argument('-p','--port', type=int, help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_argument('--iface', help=help, default='localhost')

    help = "The number of seconds between sending bytes."
    parser.add_argument('--delay', type=float, help=help, default=.1)

    help = "The number of bytes to send at a time."
    parser.add_argument('--num-bytes', type=int, help=help, default=20)

    parser.add_argument('poetry_file')

    args = vars(parser.parse_args())

    poetry_file = args['poetry_file']
    if not poetry_file:
        parser.error('No such file: %s' % poetry_file)

    return args


def send_poetry(sock, poetry_file, num_bytes, delay,inputf):
    """Send some poetry slowly down the socket."""

    bytes = inputf.read(num_bytes)

    if not bytes:
        sel.unregister(sock)
        sock.close()
        inputf.close()
        print('sending complete')
        return True

    try:
        sock.sendall(bytes)
    except socket.error:
        sel.unregister(sock)
        sock.close()
        inputf.close()
        print('some error, sending stoped')
        return False

    time.sleep(delay)


def serve(listen_socket, poetry_file, num_bytes, delay):
    sock, addr = listen_socket.accept()
    print('Somebody at %s wants poetry!' % (addr,))
    sock.setblocking(False)

    inputf = open(poetry_file,'rb')
    sel.register(sock,selectors.EVENT_WRITE,
        data={'callback':send_poetry,'args':[poetry_file,num_bytes,delay,inputf]})


def main():
    args= parse_args()
    poetry_file = args['poetry_file']
    port = args['port']
    iface = args['iface']
    num_bytes = args['num_bytes']
    delay = args['delay']

    sock = socket.socket()
    sock.bind((iface, port or 0))
    sock.listen(100)
    sock.setblocking(False)
    print('Serving %s on port %s.' % (poetry_file, sock.getsockname()[1]))

    sel.register(sock, selectors.EVENT_READ,
        data={'callback':serve,'args':[poetry_file,num_bytes,delay]})

    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data['callback']
            callback(key.fileobj, *key.data['args'])

    sock.close()


if __name__ == '__main__':
    main()
