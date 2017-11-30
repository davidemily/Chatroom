
import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 10528
connections = 0
loginFlag = 0

host = input("What is the host name? ")

print ("Trying to connect to chat server...")
while connections == 0:
    try:
        sock.connect((host, port))
        connections = connections + 1
    except:
        pass
print("")
print("#######################")
print("## You're connected! ##")
print("#######################")

print("")
print("Type 'login username password' to login")
print("Type 'newuser username password' to create a newuser")
print("Type 'send' to send a message")
print("Type 'logout' to logout")
print("Type 'menu' to print this menu again")
print("")

while (loginFlag == 0):
    message = input(">> ")
    sock.send(message.encode())
    message = sock.recv(1024).decode()
    ##########################
    ### checking for login ###
    ##########################
    if "Server: " in message:
        if " joins" in message: #login message would contain these two words
            newUsername = message.split(" ")[1]
            loginFlag =1 # if login good, pump counter to get name next to input
    print(message)

while(loginFlag == 1):
    message = input(newUsername+">> ")
    sock.send(message.encode())
    message = sock.recv(1024).decode()
    #########################
    ## checking for logout ##
    if "Server: " in message:
        if " left" in message:
            print(message)
            break
    print(message)

print("")
print("Please come again!")
sock.close()
