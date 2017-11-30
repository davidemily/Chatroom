import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10528

sock.bind((host,port))
sock.listen(3)
print("#################################################")
print ("Chat server started on host: " +host+ " on port: " + str(port))
print("#################################################")
print("")
print ("Waiting for connection")

addr = sock.accept()

print("Client " +str(addr[0])+ "has connected!")

input()
