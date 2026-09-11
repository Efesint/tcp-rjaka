import socket
import os
import sys

import time

os.system("clear")
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



