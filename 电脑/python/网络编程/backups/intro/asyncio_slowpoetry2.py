#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, time
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
    parser.add_argument('--iface', help=help, default='127.0.0.1')

    help = "The number of bytes to send at a time."
    parser.add_argument('--num-bytes', type=int, help=help, default=20)


    parser.add_argument('poetry_file')

    args = vars(parser.parse_args())

    poetry_file = args['poetry_file']
    if not poetry_file:
        parser.error('No such file: %s' % poetry_file)

    return args


class PoetryServeProtocol(asyncio.Protocol):

    def __init__(self,inputf,num_bytes):
        self.inputf = inputf
        self.num_bytes = num_bytes


    def connection_made(self,transport):
        self.transport = transport
        print(self.transport)

    def data_received(self,data):
        if data == b'poems':
            poem = self.inputf.read(self.num_bytes)
            if poem:
                self.transport.write(poem)
            else:
                self.transport.write_eof()

def main():
    args= parse_args()
    poetry_file = args['poetry_file']
    num_bytes = args['num_bytes']
    port = args['port']
    iface = args['iface']

    inputf = open(poetry_file,'rb')

    eventloop = asyncio.get_event_loop()

    print(iface,port)
    coro = eventloop.create_server(lambda:PoetryServeProtocol(inputf,num_bytes),iface,port)

    server = eventloop.run_until_complete(coro)
    print(server)

    try:
        eventloop.run_forever()
    finally:
        eventloop.close()


if __name__ == '__main__':
    main()
