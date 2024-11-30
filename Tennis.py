import socket
import sys
import argparse
import random

parser=argparse.ArgumentParser()
parser.add_argument("-l", help="The Port the application should listen on. Default 4456")
parser.add_argument("-i", help="The IP the application should pass on to. If not set, the application instead adds spin and returns to the client.")
parser.add_argument("-p", help="The Port the application should pass on to. If not set, the application instead adds spin and returns to the client.")
parser.add_argument("--AddSpin", help="--AddSpin: Only relevant if lauched as a proxy. If this flag is set, spin is added before sending to the next server and returning back to the client, effectively turning it into a chain.", action='store_true')
parser.add_argument("-d", help="One in N Packages is dropped for testing purposes. Default 0 so no packages are dropped.")
args=parser.parse_args()

listenPort = 4457
sendToPort = 0
dropPerN = 0
rootNode = False
maxAttemps = 4

if args.l:
    listenPort = int(args.l)
if args.d:
    dropPerN = int(args.d)
if args.i:
    ip = args.i
else:
    rootNode = True
    args.AddSpin = True
if args.p:
    sendTo = int(args.p)
else:
    rootNode = True
    args.AddSpin = True

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', listenPort))

def reply(spin):
    dropPackage = False
    if (dropPerN > 0):
        if random.randint(1, dropPerN) == 1:
            dropPackage = True

    for attempts in range(maxAttemps):
        try:
            if dropPackage:
                raise Exception("Debug error") 
            else:
                server_socket.sendto(spin.to_bytes(2, 'big'), address)
        except Exception as e: 
            print(f"{e}\nRetrying...")
            if (attempts > maxAttemps):
                continue
        else:
            break

def passOn(spin):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    addr = (ip, sendToPort)

    for attempts in range(maxAttemps):
        try:
            print(f"sending spin : {spin}")
            message = spin.to_bytes(2, 'big')
            client_socket.sendto(message, addr)
            data, server = client_socket.recvfrom(2)
            received = int.from_bytes(data, 'big')
            print(f"received spin : {received}")
            return received
        except socket.timeout:
            print("REQUEST TIMED OUT\nRetrying...")
            if (attempts > maxAttemps):
                continue
        except Exception as e:
            print(f"{e}\nRetrying...")
            if (attempts > maxAttemps):
                continue
        else:
            break

while True:
    try:
        message, address = server_socket.recvfrom(1024)
        spin = int.from_bytes(message, 'big')
        print(f"received from client: {spin}")
        if args.AddSpin:
            spin += 1
        if not rootNode:
            spin = passOn(spin)
            if args.AddSpin:
                spin += 1
        print(f"sending to client: {spin}")
        reply(spin)
    except Exception as e:
        print(f"{e}")
