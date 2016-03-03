import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("127.0.0.1", 30081)
sock.connect(server_addr)
sock.sendall("from client\n")
data = sock.recv(1024)
sock.close()
print "receiverd:",repr(data)
