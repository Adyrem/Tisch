import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO add default value in case no argument is passed
# TODO change to named argument instead
server_socket.bind(('', int(sys.argv[1])))

while True:
    # TODO add parsing, error handling and data transformation
    message, address = server_socket.recvfrom(1024)
    server_socket.sendto(message, address)
