import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10528
loginFlag = 0
sock.bind((host,port))
sock.listen(3)
print("")
print("")
print("##############################################################")
print ("## Chat server started on host: " +host+ " on port: " + str(port) + "##")
print("##############################################################")
print("")
print("")
print ("Waiting for connection...")

conn, addr = sock.accept()

print("")
print("Client " + str(addr[0]) + "has connected!")
print("")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    if(data.split(" ")[0].lower == "login"):
        print("")
        newUsername = data.split(" ")[1]
        newPassword = data.split(" ")[2]
        data = "Login failed. Please check username and password."
        with open("login.txt", "r") as f:
            for line in f:
                if newUsername in line:
                    if newPassword in line:
                        print(newUsername + " login")
                        data = "Server: " + newUsername + " joins"
                        loginFlag = 1
        conn.send(data.encode())

    if(data.split(" ")[0].lower == "send"):
        print("")
        if(loginFlag == 0):
            data = "Server: Denied. Please Login First"
        else:
            data = newUsername + ": " + data[5:]
            print (newUsername + ": " + data[5:0])
        conn.send(data.encode())

    if(data.split(" ")[0].lower() == "newuser"

conn.close()
