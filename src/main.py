#!/usr/bin/python
"""
write by efesint in sept 2026.
the software is released under the GPL license.
The software is distributed without ANY warranty, and the author bears no liability whatsoever.
"""

import socket
import os
import sys
import ipaddress

from concurrent.futures import ThreadPoolExecutor

import time

art = r"""
 ______________          ___     _____   __ _____ 
/_  __/ ___/ _ \  ____  / _ \__ / / _ | / //_/ _ |
 / / / /__/ ___/ /___/ / , _/ // / __ |/ ,< / __ |
/_/  \___/_/          /_/|_|\___/_/ |_/_/|_/_/ |_|
"""

run = True

def check_con():
    try: 
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def menu():
    os.system("clear")     
    print(art)
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

    print("What should be done?")
    print("\u001b[31m")


    print("[1] scan tcp ports")
    print("[2] test (scan your own ip)")
    print("[0] exit\n")

def scan():
    while True:
        print("Write the IPv4 address to scan\n")
        ip = input()
        try:
            ipaddress.IPv4Address(ip)
            break
        except ipaddress.AddressValueError:
            print("\nx")
        
    print("[x]", ip)
    
menu()

while run == True:
    try:
        choise = int(input())
    except ValueError:
        print("Enter the number")
        continue
    if choise == 1:
        scan()
    elif choise == 0:
        print("exiting the programm..\n")
        run = False
