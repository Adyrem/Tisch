# Tisch Ping Project

Tisch is a school project for writing a ping protocol by hand.
Tisch is the Client with Tennis being the server.

## Using Tisch

Tisch.py (Ping) is the client application.

Arguments:
```
-i: The server the application should try to ping. Default localhost
-p: The Port the application should send to. Default 4456
```
Example Usage:
```
python Tisch.py -i="127.0.0.1" -p=4456
```

## Using Tennis

Tennis.py (Pong) is the server application. It can also be used as a client in a chain or as a proxy. See arguments for details.

Arguments:
```
-l: The Port the application should listen on. Default 4456
-i: The IP the application should pass on to. If not set, the application instead adds spin and returns to the client.
-p: The Port the application should pass on to. If not set, the application instead adds spin and returns to the client.
--AddSpin: Only relevant if lauched as a proxy. If this flag is set, spin is added before sending to the next server and returning back to the client, effectively turning it into a chain.
-d: One in N Packages is dropped for testing purposes. Default 0 so no packages are dropped.
```
Example server:
```
python Tennis.py -l=4456
```
Example proxy:
```
python Tennis.py -l=4456 -p=4457 -i="127.0.0.1"
```
Example chain:
```
python Tennis.py -l=4456 -p=4457 -i="127.0.0.1" --AddSpin
```