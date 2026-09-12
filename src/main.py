import socket
import os
import sys
import subprocess

import time

art = r"""
 ______________          ___     _____   __ _____ 
/_  __/ ___/ _ \  ____  / _ \__ / / _ | / //_/ _ |
 / / / /__/ ___/ /___/ / , _/ // / __ |/ ,< / __ |
/_/  \___/_/          /_/|_|\___/_/ |_/_/|_/_/ |_|
"""

def check_con():
    try: 
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

os.system("clear")     

if check_con():
   print("\033[32m")
   print("[+] Internet connection is stable.")
else:
   time.sleep(1)
   print("\033[31m")
   print("[-] No internet connection.")
   print("[-] Exiting the program")
   sys.exit(1)

print("\033[90m")
print(art)

run = True
print("What should be done?")
print("\u001b[31m")

print("\n[1] Scan tcp ports")
print("[0] exit\n")

while run == True:
    try:
        choise = int(input())
    except ValueError:
        print("Enter the number")
        continue
    if choise == 1:
        print("\nWrite the ip address to scan\n")
        ip = input()
        print("\n[x]", ip) 
    elif choise == 0:
         print("exiting the programm..")
         run = False
