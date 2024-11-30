import socket
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i", help="The server the application should try to ping. Default localhost")
parser.add_argument("-p", help="-i: -p: The Port the application should send to. Default 4456")
args=parser.parse_args()

ip = "127.0.0.1"
port = 4456

if args.i:
    ip = args.i
if args.p:
    port = int(args.p)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = (ip, port)

#Dont try to recover failed pings. Instead just ping 4 seperate times
for pings in range(4):
    try:
        spin = 1
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
