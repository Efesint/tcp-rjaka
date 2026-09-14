#!/usr/bin/python
"""
write by efesint in sept 2026.
the software is released under the GNU General Public License v3.0.
The software is distributed without ANY warranty, and the author bears no liability whatsoever.
"""
import socket
import os
import sys
import ipaddress
import requests
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
    print("\033[31m" + art + "\033[0m")
    if check_con():
        print("\033[32m[+] Internet connection is stable.\033[0m\n")
    else:
        time.sleep(1)
        print("\n\033[31m[-] No internet connection.\033[0m")
        print("\033[31m[-] Exiting the program\033[0m\n")
        sys.exit(1)

    print("\033[31mWhat should be done?\033[0m")
    print("\033[31m[1] scan tcp ports\033[0m")
    print("\033[31m[2] get info about ip address\033[0m")
    print("\033[31m[0] exit\033[0m\n")


def scan():
    while True:
        print("\033[31mWrite the IPv4 address to scan\033[0m")
        ip = input().strip()
        try:
            ipaddress.IPv4Address(ip)
            break
        except ipaddress.AddressValueError:
            print("\n\033[31m[!] Invalid IP address. Try again.\033[0m\n")

    print("\033[31m[x] Target IP: " + ip + "\033[0m\n")
    print("\033[31mWrite the first port:\033[0m")
    fport = int(input())

    print("\033[31mWrite the end port:\033[0m")
    eport = int(input())

    print("\n\033[31m[*] Scanning started on " + ip + "\033[0m")
    start_time = time.time()

    for port in range(fport, eport + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("\033[31m[+] Port " + str(port) + " is open\033[0m")
        sock.close()

    print("\n\033[31m[x] Scanning finished.\033[0m\n")


def get_info(ip):
    try:
        response = requests.get(
            url=f'http://ip-api.com/json/{ip}',
            timeout=5
        ).json()

        if response.get('status') == 'fail':
            print("\033[31m[x] Error: unknown\033[0m")
            return None

        data = {
            'IP': response.get('query'),
            'Organization': response.get('org'),
            'Provider': response.get('isp'),
            'Region Name': response.get('regionName'),
            'Country': response.get('country'),
            'City': response.get('city'),
            'Lat': response.get('lat'),
            'Lon': response.get('lon'),
        }

        print("\n\033[31m═══════════════════════════════════\033[0m")
        for k, v in data.items():
            print("\033[31m    " + str(k) + ": " + str(v) + "\033[0m")
        print("\033[31m═══════════════════════════════════\033[0m\n")

        return data

    except requests.exceptions.ConnectionError:
        print("\033[31m[x] Check your internet connection\033[0m")
        return None
    except requests.exceptions.Timeout:
        print("\033[31m[x] Timeout\033[0m")
        return None
    except requests.exceptions.RequestException as e:
        print("\033[31m[x] Error of request\033[0m")
        return None


menu()

while run == True:
    try:
        choise = int(input())
    except ValueError:
        print("\n\033[31mEnter the number\033[0m\n")
        continue

    if choise == 1:
        scan()
    elif choise == 2:
        print("\033[31mWrite the IPv4 address\033[0m")
        ipv4 = input()
        get_info(ipv4)
    elif choise == 0:
        print("\n\033[31mexiting the programm..\033[0m\n")
        run = False
