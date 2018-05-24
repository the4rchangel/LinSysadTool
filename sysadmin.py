#!/bin/#!/usr/bin/env python3
# https://www.bggofurther.com/2015/01/create-an-interactive-command-line-menu-using-python/
# https://stackoverflow.com/questions/34192588/simple-menu-in-python-3
#https://stackoverflow.com/questions/3190955/how-to-create-a-user-in-linux-using-python

import sys, os, getpass
#Sudo check
if os.geteuid() != 0:
    exit("\033[0;31;47m You need to have root privileges to run this script.\nPlease try again using your sysadmin 'sudo' powers. \nExiting.")


ans=True
while ans:
    print ("""
####################################################
#            Archangel's Sysadmin Tool             #
#            twitter.com/the4rchangel              #
#                v0.1 (May 2018)                   #
#                                                  #
#            WHAT WOULD YOU LIKE TO DO?            #
####################################################

    1> User / Group Settings (Add | Remove | Passwords | Etc.)
    2> System Tools (Memory | Logs | Cron | Etc.)
    3> Networking (Traffic Analysis | IP Tables | Logs | Etc.)
    4> Security (what tools would I want?)
    5> Have you tried turning it off and on again? (Restart)
    6> Exit/Quit
    """)
    ans=raw_input("Please select an option: ")
    if ans=="1":
      os.system('clear')
      ans1=True
      while ans1:
          print("""
          1> Add user
          2> Delete user
          3> List users
          3> Change user password
          4> Add user to group
          5> Remove user from group
          6> Create group
          7> List groups
          """)
          ans1=raw_input("Please select an option: ")
          if ans1=="1":
              name= raw_input("What is their full name: ")
              uname= raw_input("What is the username: ")
              password= getpass.getpass('What password would you like to assign: ')
              os.system("useradd -p "+password+" -s "+ "/bin/bash "+ "-d "+ "/home/" + uname+ " -m "+ " -c \""+ name+"\" " + uname)
              print ("New user "+name+ " added!")
	  if ans1=="2":
              uname= raw_input("What is the username: ")
              delhome= raw_input("Would you like to delete their home folder (y/n): ")
              os.system("useradd -p "+password+" -s "+ "/bin/bash "+ "-d "+ "/home/" + uname+ " -m "+ " -c \""+ name+"\" " + uname)
              print ("New user "+name+ " added!")
      print("\n USER ADDED")
    elif ans=="2":
      print("\n Student Deleted")
    elif ans=="3":
      print("\n Student Record Found")
    elif ans=="6":
      print("\n Goodbye")
      break
    elif ans !="":
      print("\n I hate this hacker crap! Try again.")



#Input elements for re-use throughout program (CONFIRMED WORKING)
#uname= raw_input("What is the username: ")
#password= getpass.getpass('What password would you like to assign: ')
#print ("The username you selected is ") + uname
#print ("The password you inputted is ") + password
