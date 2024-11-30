import socket
import sys
import argparse
import random

parser=argparse.ArgumentParser()
parser.add_argument("-p", help="Port to listen on")
parser.add_argument("-d", help="Randomly drops one in N packages to test error handling")
args=parser.parse_args()

port = 4456
drop = 0
if args.p:
    port = int(args.p)
if args.d:
    drop = int(args.d)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', port))

while True:
    try:
        message, address = server_socket.recvfrom(1024)
        message = (int.from_bytes(message, 'big') + 1).to_bytes(2, 'big')
        if (drop > 0):
            if random.randint(0, drop) != 0:
                server_socket.sendto(message, address)
        else:
            server_socket.sendto(message, address)
    except Exception as e:
        print(f"{e}")
