#!/usr/bin/env python3
# https://www.bggofurther.com/2015/01/create-an-interactive-command-line-menu-using-python/
# https://stackoverflow.com/questions/34192588/simple-menu-in-python-3

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
	ans=input("Please select an option: ")
#User / Group Settings
	if ans=="1":
		os.system('clear')
		print("""
          1> Add user
          2> Delete user
          3> List users
          4> Change user password
          5> List groups
          6> Add user to group
          7> Remove user from group
          8> Create group
	  9> Return to previous menu
          """)
		ans1=input("Please select an option: ")
		if ans1=="1":
			os.system("clear")
			name= input("What is their full name: ")
			uname= input("What is the username: ")
			password= getpass.getpass('What password would you like to assign: ')
			os.system("useradd -p "+password+" -s "+ "/bin/bash "+ "-d "+ "/home/" + uname+ " -m "+ " -c \""+ name+"\" " + uname)
			os.system('clear')
			print ("New user "+name+ " added!")
		if ans1=="2":
			os.system("clear")
			uname= input("What is the username: ")
			delhome= input("Would you like to delete their home folder (y/n): ")
			if delhome=="y":
				os.system("rm -rf "+uname)
			elif delhome=="n":
				os.system("mv /home/"+uname+ " /var/backups/"+uname)
				os.system("userdel "+uname)
				os.system('clear')
				print ("User "+uname+ " removed!")
		if ans1=="3":
			os.system("clear")
			os.system("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1")
		if ans1=="4":
			os.system("clear")
			uname= input("Which user's password would you like to reset: ")
			pwreset= input("Do you want to force a change on next login (y/n): ")
			if pwreset=="n":
				os.system("passwd "+uname)
			if pwreset=="y":
				os.system("passwd "+uname)
				os.system("chage -d 0 "+uname)
				os.system("clear")
				print ("Password change successful!")
		if ans1=="5":
			os.system("clear")
			os.system("getent group")
		if ans1=="6":
			os.system("clear")
			uname= input("Which username would you like to add to a group: ")
			groupadd= input("Which group would you like to add them to: ")
			os.system("usermod -a -G "+groupadd+ " "+uname)
			os.system("clear")
			print(uname + " added to "+ groupadd)
		if ans1=="7":
			os.system("clear")
			uname= input("Which username would you like to remove from a group: ")
			grouprem= input("Which group would you like to remove them from: ")
			os.system("gpasswd -d "+uname+ " "+grouprem)
			os.system("clear")
			print(uname + " removed from "+ grouprem)
		if ans1=="8":
			os.system("clear")
			groupname= input("What would you like the group to be named: ")
			os.system("groupadd "+groupname)
			os.system("clear")
			print(groupadd +" added as a group!")
		if ans1=="9":
			os.system("clear")
			break
		else:
			print("\n I hate this hacker crap! Try again.")

#System Settings
	elif ans=="2":
		os.system("clear")
		print("\n Option 2 Not Complete")
#Networking Settings
	elif ans=="3":
		os.system("clear")
		print("\n Option 3 Not Complete")
#Security Settings
	elif ans=="4":
		os.system("clear")
		print("\n Option 4 Not Complete")
#Reboot Option
	elif ans=="5":
		os.system("clear")
		doit= input("Are you sure you'd like to reboot (y/n): ")
		if doit=="n":
			break
		if doit=="y":
			os.system("reboot")
#Exit Program
	elif ans=="6":
		os.system("clear")
		print("\n Goodbye")
		break
	elif ans !="":
		os.system("clear")
		print("\n I hate this hacker crap! Try again.")    
