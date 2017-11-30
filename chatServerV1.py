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
print("###############################################################")
print ("## Chat server started on host: " +host+ " on port: " + str(port) + " ##")
print("###############################################################")
print("")
print("")
print ("Waiting for connection...")

conn, addr = sock.accept()

print("")
print("Client " + str(conn) + "has connected!")
print("")

while True:
    data = conn.recv(1024).decode()

    if(data.split(" ")[0] == "login"):
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
        f.close()
        conn.send(data.encode())

    if(data.split(" ")[0] == "send"):
        if(loginFlag == 0):
            data = "Server: Denied. Please Login First"
        else:
            data = newUsername + ": " + data[5:]
            print (newUsername + ": " + data[5:])
        conn.send(data.encode())

    if(data.split(" ")[0] == "newuser"):
        createUsername = data.split(" ")[1]
        createPassword = data.split(" ")[2]
        f = open('login.txt', 'a')
        f.write(createUsername + " " + createPassword +'\n')
        f.close()
        print("New user " + createUsername + " created")
        data = "New user " + createUsername + " created"
        conn.send(data.encode())

    if(data.split(" ")[0] == "logout"):
        print(newUsername + " logout")
        data = "Server: " + newUsername + " left."
        conn.send(data.encode())

    if not data:
        break

conn.close()
