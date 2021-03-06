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
host = socket.gethostname()
port = 10528
loginFlag = 0
sock.bind((host,port))
sock.listen(3) # set for 3 connections but it only handles one

#####################################################
#      Formatting for when the server starts up     #
#####################################################
print("")
print("")
print("###############################################################")
print ("## Chat server started on host: " +host+ " on port: " + str(port) + " ##")
print("###############################################################")
print("")
print("")
print ("Waiting for connection...")

conn, addr = sock.accept() #accepts connects from anyone

################################################
##        Formatting for a user joining       ##
################################################
print("")
print("Client " + str(conn) + "has connected!")
print("")


############################################
##  Handles all of the traffic from user  ##
###   in a while loop to make it easy    ###
############################################
while True:
    data = conn.recv(1024).decode()
    testWord = data.split(" ")[0]

    ################################
    ##        Login Function      ##
    ################################
    if(testWord == "login"):
        if(loginFlag !=0):
            data = "Server: " + newUsername + " is already logged in!"
        else:
            try:
                newUsername = data.split(" ")[1]
                newPassword = data.split(" ")[2]
                print("Login Failed.")
                data = "Login failed. Please check username and password."
                with open("login.txt", "r") as f:
                    for line in f:
                        if newUsername in line:
                            if newPassword in line:
                                print(newUsername + " login")
                                data = "Server: " + newUsername + " joins"
                                loginFlag = 1
            except:
                data = "Login failed. Please check username and password."
            finally:
                f.close()
        conn.send(data.encode())

    ################################
    ##        Send  Function      ##
    ################################
    elif(testWord == "send"):
        if(loginFlag == 0):
            data = "Server: Denied. Please Login First"
        else:
            data = newUsername + ": " + data[5:]
            print (newUsername + " " + data[5:])
        conn.send(data.encode())

    ################################
    ##       New User Function    ##
    ################################
    elif(testWord == "newuser"):
        print("Attempt to create new user...")
        try:
            createUsername = data.split(" ")[1]
            createPassword = data.split(" ")[2]
            if len(createUsername)<32 and len(createPassword)>3 and len(createPassword)<8:
                f = open('login.txt', 'a')
                if createUsername not in f:
                    f.write(createUsername + " " + createPassword +'\n')
                    f.close()
                    print("New user " + createUsername + " created")
                    data = "New user " + createUsername + " created"

            else:
                print("Problem creating new account")
                data = "Did not follow requirements"
        except:
            print("Did not include enough arguements")
            data = "Did not include enough arguments or account exists"

        finally:
            conn.send(data.encode())

    ################################
    ##       Logout Function      ##
    ################################
    elif(testWord == "logout"):
        if(loginFlag == 0):
            data = "You're not logged in"
            conn.send(data.encode())
        else:
            print(newUsername + " logout")
            data = "Server: " + newUsername + " left."
            conn.send(data.encode())
            loginFlag = loginFlag - 1

    ################################
    ##        Quit Function       ##
    ################################
    elif(testWord == "quit"):
        if(loginFlag==0):
            print("Server: " + str(conn) + " has decided to quit!")
            data = "Server: " + str(conn) + " has decided to quit!"
        else:
            data = "Server: " + newUsername + " has decided to quit!"
        conn.send(data.encode())
        break
    ################################
    ##      Error   Function      ##
    ################################
    else:
        print("Couldn't read input")
        data = "Server: couldn't read input"
        conn.send(data.encode())

    ################################
    ##       Socket Closes        ##
    ################################
    if not data:
        break


#######################
# End of program when #
## while loops fails ##
#######################
print("")
print("Client " + str(conn) + "has disconnected!")
conn.close()
print("")
print("Exiting server...")
print("")
