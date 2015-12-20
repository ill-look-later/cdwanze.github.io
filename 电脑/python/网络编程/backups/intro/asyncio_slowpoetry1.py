#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, socket, time
import asyncio

def parse_args():
    usage = """usage: %prog [options] poetry-file

This is the Slow Poetry Server, blocking edition.
Run it like this:

  python3 asyncio_slowpoetry3.py ecstasy.txt

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


def send_poetry(eventloop,sock, poetry_file, num_bytes, delay,inputf):
    """Send some poetry slowly down the socket."""

    bytes = inputf.read(num_bytes)

    if not bytes:
        eventloop.remove_writer(sock)
        sock.close()
        inputf.close()
        print('sending complete')
        return True

    try:
        sock.sendall(bytes)
    except socket.error:
        eventloop.remove_writer(sock)
        sock.close()
        inputf.close()
        print('some error, sending stoped')
        return False

    time.sleep(delay)


def serve(eventloop,listen_socket, poetry_file, num_bytes, delay):
    sock, addr = listen_socket.accept()
    print('Somebody at %s wants poetry!' % (addr,))
    sock.setblocking(False)

    inputf = open(poetry_file,'rb')
    eventloop.add_writer(sock, send_poetry, eventloop,sock,poetry_file,num_bytes,delay,inputf)


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

    eventloop = asyncio.get_event_loop()
    eventloop.add_reader(sock,serve,eventloop,sock,poetry_file,num_bytes,delay)

    try:
        eventloop.run_forever()
    finally:
        eventloop.close()

    sock.close()


if __name__ == '__main__':
    main()
