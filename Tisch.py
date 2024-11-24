import socket
import sys

spin = 1

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = spin.to_bytes(2, 'big')

    # TODO add default value in case no argument is passed
    # TODO change to named argument instead
    addr = (sys.argv[1], int(sys.argv[2]))

    print(f"sending spin : {spin}")
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        spin = int.from_bytes(data, 'big')
        print(f"received spin : {spin}")
        spin += 1
    except socket.timeout:
        print('REQUEST TIMED OUT')
