import socket
import sys

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    # TODO change payload to actual data
    message = b'test'

    # TODO add default value in case no argument is passed
    # TODO change to named argument instead
    addr = (sys.argv[1], int(sys.argv[2]))

    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        print(f'{data} {pings}')
    except socket.timeout:
        print('REQUEST TIMED OUT')