import socket
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i", help="IP to ping")
parser.add_argument("-p", help="Port to ping")
args=parser.parse_args()

ip = args.i
port = int(args.p)
spin = 1

if ip == "":
    ip = "127.0.0.1"
if port == 0:
    port = 4456

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = (ip, port)

for attempts in range(4):
    try:
        print(f"sending spin : {spin}")
        message = spin.to_bytes(2, 'big')
        client_socket.sendto(message, addr)
        data, server = client_socket.recvfrom(1024)
        spin = int.from_bytes(data, 'big')
        print(f"received spin : {spin}")
        spin += 1
    except socket.timeout:
        print("REQUEST TIMED OUT")
    except Exception as e:
        print(f"{e}")
