#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime, argparse
import asyncio

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


class PoetryClientProtocol(asyncio.Protocol):

    def __init__(self,infile):
        self.infile = infile

    def connection_made(self,transport):
        print(transport.get_extra_info('peername'))
        self.transport = transport
        self.transport.write(b'poems')

    def data_received(self, data):
        if data:
            print(data)
            print('writing to {}'.format(self.infile.name))
            self.infile.write(data)
            self.transport.write(b'poems')
    def eof_received(self):
            print('end of writing')
            self.infile.close()


def main():
    addresses = parse_args()
    eventloop = asyncio.get_event_loop()

    for address in addresses:
        host, port = address
        filename = str(port) + '.txt'
        infile = open(filename,'wb')
        coro = eventloop.create_connection(lambda:PoetryClientProtocol(infile),host, port)
        t,p = eventloop.run_until_complete(coro)
        print(t,p)

    try:
        eventloop.run_forever()
    finally:
        eventloop.close()


if __name__ == '__main__':
    main()
