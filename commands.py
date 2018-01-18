# Copyright (c) 2018, Kevin Rodgers
# Released subject to GNU Lesser General Public License v3
# Please see http://www.gnu.org/licenses
import sys
import json
import getopt
import rest_client


class NgrokCommError(Exception):
    def __init__(self, message):
        self.message = message
        super(NgrokCommError, self).__init__(message)


def print_to_err(message):
    sys.stderr.write(message + '\n')


def get_tunnels():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'n:', [])
    except getopt.GetoptError as err:
        print_to_err(str(err))
        sys.exit(1)

    name = None
    for opt, arg in options:
        if opt == '-n':
            name = arg
        else:
            print_to_err('%s: Invalid option' % opt)
            sys.exit(1)

    url = 'api/tunnels'
    if name is not None:
        url = 'api/tunnels/%s' % name

    status, response = rest_client.get_url(url)
    if status != 200:
        print_to_err(repr(response))
        raise NgrokCommError('GET failed, %d' % status)

    print json.dumps(response, indent=4)


def start_tunnel():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'n:h:p:P:r:', [])
    except getopt.GetoptError as err:
        print_to_err(str(err))
        sys.exit(1)

    name = None
    host = '127.0.0.1'
    port = 80
    proto = 'http'
    remote_addr = None
    for opt, arg in options:
        if opt == '-n':
            name = arg
        elif opt == '-h':
            host = arg
        elif opt == '-p':
            port = int(arg)
        elif opt == '-P':
            proto = arg
        elif opt == 'r':
            remote_addr = arg
        else:
            print_to_err('%s: Invalid option' % opt)
            sys.exit(1)

    if name is None:
        print_to_err('Must specify a name')
        sys.exit(2)

    params = dict(name=name, addr='%s:%d' % (host, port), proto=proto)
    if remote_addr is not None:
        params['remote_addr'] = remote_addr

    status, response = rest_client.post_url('api/tunnels', params=params)
    if status != 201:
        print_to_err(repr(response))
        raise NgrokCommError('POST failed, %d' % status)

    print json.dumps(response, indent=4)


def delete_tunnel():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'n:', [])
    except getopt.GetoptError as err:
        print_to_err(str(err))
        sys.exit(1)

    name = None
    for opt, arg in options:
        if opt == '-n':
            name = arg
        else:
            print_to_err('%s: Invalid option' % opt)
            sys.exit(1)

    if name is None:
        print_to_err('Must specify a name')
        sys.exit(2)

    status, response = rest_client.delete_url('api/tunnels/%s' % name)
    if status != 204:
        print_to_err(repr(response))
        raise NgrokCommError('DEL failed, %d' % status)

    print json.dumps(response, indent=4)


def list_requests():
    status, response = rest_client.get_url('api/requests/http')
    if status != 200:
        print_to_err(repr(response))
        raise NgrokCommError('GET failed, %d' % status)

    print json.dumps(response, indent=4)


if __name__ == '__main__':
    get_tunnels()
