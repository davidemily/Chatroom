######################################################################
## David Emily #######################################################
## CS 4850 ###########################################################
## Lab 3 #############################################################
## Description: ######################################################
## In this lab we created a server and client message application. ###
## The program runs on Python's Socket and Sys libraries. ############
## The server expects a socket request on a certain port. ############
## When the client also requests the socket from the server, #########
## a connection is made that can be used for sending data, ###########
## in this case, messages. The server then echos the message #########
## back to the client to show that the socket works both ways. #######
## I implemented a very bare version of this room in order ###########
## to complete the requirements of Lab 3 version 1 ###################
## I've never used Python before but I chose the language due to #####
## huge amount of resources available and the low learning curve #####
######################################################################

import socket
import sys
import time

#######################################################
###    Creating a socket using Python Socket & Sys  ###
#######################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 10528
connections = 0
loginFlag = 0
print("")
host = input("What is the host name? ")

print ("")
print ("Trying to connect to chat server...")
while connections == 0:
    try:
        sock.connect((host, port))
        connections = connections + 1
    except:
        pass

#####################################################
#      Formatting for when the client connects      #
#####################################################
print("")
print("#######################")
print("## You're connected! ##")
print("#######################")

print("")
print("Type 'login username password' to login")
print("Type 'newuser username password' to create a newuser")
print("           username must be less than 32 characthers")
print("           password must be between 4 & 8 characters")
print("Type 'send' to send a message")
print("Type 'logout' to logout")
print("Type 'quit' to shutdown service")
print("")

## While loop to run the program
while(True):
    if (loginFlag == 0): ##check if logged in or not
        message = input(">> ")
        sock.send(message.encode()) # python3 defaults to UTF-8 encoding for socket
        message = sock.recv(1024).decode() # decoding what is received by the server

        ##########################
        ### checking for login ###
        ##########################
        if message.split(" ")[0] == "Server:" and message.split(" ")[2] == "joins":
            #if message.split(" ")[2] == "joins" #login message would contain these two words
            newUsername = message.split(" ")[1]
            loginFlag = 1 # if login good, pump counter to get name next to input

        ##########################
        ### checking for quit  ###
        ##########################
        elif message.split(" ")[0] == "Server:" and "has decided to quit!" in message:
            print(message)
            break

        print(message)

##################################
### if statement after log in  ###
# used to add login name to chat #
##################################
    if(loginFlag == 1): ##used for when logged in
        message = input(newUsername+">> ")
        sock.send(message.encode())
        message = sock.recv(1024).decode()
        #########################
        ## checking for logout ##
        #########################
        if message.split(" ")[0] == "Server:" and "left" in message:
            loginFlag = 0
        elif message.split(" ")[0] == "Server:" and "has decided to quit!" in message:
            print(message)
            break
        print(message)

##############################
##### while loops exited #####
## close socket and program ##
##############################
print("")
print("Please come again!")
print("")
sock.close()
