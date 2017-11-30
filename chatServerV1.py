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

    ######################
    ##  Login Function  ##
    ######################

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
        f.close()
        conn.send(data.encode())

    ######################
    ##  Send  Function  ##
    ######################

    if(data.split(" ")[0].lower == "send"):
        print("")
        if(loginFlag == 0):
            data = "Server: Denied. Please Login First"
        else:
            data = newUsername + ": " + data[5:]
            print (newUsername + ": " + data[5:0])
        conn.send(data.encode())

    #######################
    ## New User Function ##
    #######################

    if(data.split(" ")[0].lower() == "newuser"):
        print("")
        createUsername = data.split(" ")[1]
        createPassword = data.split(" ")[2]
        f = open('login.txt', 'a')
        f.write(createUsername + " " + createPassword +'\n')
        f.close()
        data = "New user " + createUsername + " created"
        conn.send(data.encode())

conn.close()
