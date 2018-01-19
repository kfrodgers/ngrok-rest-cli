# Copyright (c) 2018, Kevin Rodgers
# Released subject to GNU Lesser General Public License v3
# Please see http://www.gnu.org/licenses
import sys
import json
import getopt
import rest_client


def print_to_out(message):
    sys.stdout.write(message + '\n')


def print_to_err(message):
    sys.stderr.write(message + '\n')


def print_response_err(status, response):
    if 'details' in response and 'err' in response.get('details'):
        print_to_err(response.get('details').get('err'))
    else:
        msg = ['Status (%d): {' % status]
        for key in sorted(response.keys()):
            msg.append('    %s: %r' % (key, response[key]))
        msg.append('}')
        print_to_err('\n'.join(msg))


def remove_metrics(response):
    if 'tunnels' in response:
        for tunnel in response['tunnels']:
            if 'metrics' in tunnel:
                del tunnel['metrics']
    elif 'metrics' in response:
        del response['metrics']


def get_tunnels():
    usage = 'Usage: %s [-n <name>] [-m]' % sys.argv[0]
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'n:m', [])
    except getopt.GetoptError as err:
        print_to_err(str(err))
        sys.exit(1)

    name = None
    show_metrics = False
    for opt, arg in options:
        if opt == '-n':
            name = arg
        elif opt == '-m':
            show_metrics = True
        else:
            print_to_err('%s: Invalid option' % opt)
            print_to_err(usage)
            sys.exit(1)

    url = 'api/tunnels'
    if name is not None:
        url = 'api/tunnels/%s' % name

    status, response = rest_client.get_url(url)
    if status != 200:
        print_response_err(status, response)
        sys.exit(1)

    if not show_metrics:
        remove_metrics(response)

    print_to_out(json.dumps(response, indent=4))


def start_tunnel():
    usage = 'Usage: %s -n <name> [-h <host>] [-p <port>] [-t <tcp|http>] [-r <remote_addr>] ' % sys.argv[0]
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'n:h:p:t:r:', [])
    except getopt.GetoptError as err:
        print_to_err(str(err))
        sys.exit(1)

    name = None
    host = '127.0.0.1'
    port = 80
    tunnel = 'http'
    remote_addr = None
    for opt, arg in options:
        if opt == '-n':
            name = arg
        elif opt == '-h':
            host = arg
        elif opt == '-p':
            port = int(arg)
        elif opt == '-t':
            tunnel = arg
        elif opt == 'r':
            remote_addr = arg
        else:
            print_to_err('%s: Invalid option' % opt)
            print_to_err(usage)
            sys.exit(1)

    if name is None:
        print_to_err('Error: Must specify a name')
        print_to_err(usage)
        sys.exit(2)

    if tunnel not in ['http', 'tcp']:
        print_to_err('Error: Invalid tunnel type (%s), use http or tcp' % tunnel)
        print_to_err(usage)
        sys.exit(2)

    params = dict(name=name, addr='%s:%d' % (host, port), proto=tunnel)
    if remote_addr is not None:
        params['remote_addr'] = remote_addr

    status, response = rest_client.post_url('api/tunnels', params=params)
    if status != 201:
        print_response_err(status, response)
        sys.exit(1)

    remove_metrics(response)

    print_to_out(json.dumps(response, indent=4))


def delete_tunnel():
    usage = 'Usage: %s -n <name>' % sys.argv[0]
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
            print_to_err(usage)
            sys.exit(1)

    if name is None:
        print_to_err('Error: Must specify a name')
        print_to_err(usage)
        sys.exit(2)

    status, response = rest_client.delete_url('api/tunnels/%s' % name)
    if status != 204:
        print_response_err(status, response)
        sys.exit(1)

    # remove the auto generated http tunnel if it exists, ignore return status
    if not name.endswith(' (http)'):
        rest_client.delete_url('api/tunnels/%s (http)' % name)

    print_to_out('%s deleted' % name)


def list_requests():
    status, response = rest_client.get_url('api/requests/http')
    if status != 200:
        print_response_err(status, response)
        sys.exit(1)

    print_to_out(json.dumps(response, indent=4))


if __name__ == '__main__':
    get_tunnels()
