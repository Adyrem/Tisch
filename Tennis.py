import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO add default value in case no argument is passed
# TODO change to named argument instead
server_socket.bind(('', int(sys.argv[1])))

while True:
    # TODO add error handling
    message, address = server_socket.recvfrom(1024)

    message = (int.from_bytes(message, 'big') + 1).to_bytes(2, 'big')
    server_socket.sendto(message, address)
