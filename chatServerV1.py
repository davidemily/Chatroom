import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10528

sock.bind((host,port))
sock.listen(3)
print("#####################################################################")
print ("Chat server started on host: " +host+ " on port: " + str(port))
print("#####################################################################")
print("")
print ("Waiting for connection")

conn, addr = sock.accept()

print("")
print("Client " + str(addr[0]) + "has connected!")
print("")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    if(data.split(" ",1)[0] == "login"):
        f = open ('login.txt', 'w')
        print(f.read())
    else:
        print ("received: " + data)
        conn.send(data.encode())

conn.close()
