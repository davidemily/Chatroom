
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

print ("You're connected!")

print("")
print("Type 'login' to login")
print("Type 'newuser username password' to create a newuser")
print("Type 'send' to send a message")
print("Type 'logout' to logout")
print("Type 'menu' to print this menu again")
print("")

while (loginFlag == 0):
    message = input(">>")
    sock.send(message.encode())
    message = sock.recv(1024).decode()
    print(message)
