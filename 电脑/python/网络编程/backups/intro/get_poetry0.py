#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime, argparse, socket

def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, blocking edition.
Run it like this:

  python3 get-poetry3.py port1 port2 port3 ...

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


def get_poetry(address):
    """Download a piece of poetry from the given address."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)

    poem = b''

    while True:
        data = sock.recv(1024)

        if not data:
            sock.close()
            break
        else:
            print(data.decode('utf-8'),end='')

        poem += data

    return poem


def format_address(address):
    host, port = address
    return '%s:%s' % (host or '127.0.0.1', port)


def main():
    addresses = parse_args()
    elapsed = datetime.timedelta()

    for i, address in enumerate(addresses):
        addr_fmt = format_address(address)
        print('Task %d: get poetry from: %s' % (i + 1, addr_fmt))
        start = datetime.datetime.now()

        poem = get_poetry(address)

        time = datetime.datetime.now() - start
        msg = 'Task %d: got %d bytes of poetry from %s in %s'
        print(msg % (i + 1, len(poem), addr_fmt, time))

        elapsed += time

    print('Got %d poems in %s' % (len(list(addresses)), elapsed))


if __name__ == '__main__':
    main()
