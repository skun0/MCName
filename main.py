import requests
from colorama import Fore, init
import os
import ctypes
import sys

def check_username(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    r = requests.get(url)
    if r.status_code == 200:
        try:
            r.json()
            print(Fore.RED + f"\n[-] {username} is taken.")
        except Exception:
            print(Fore.RED + "\n[!] Unknown Error.")
    elif r.status_code in (204, 404):
        print(Fore.GREEN + f"\n[+] {username} is NOT taken")
    else:
        print(Fore.RED + f"\n[!] HTTP Error {r.status_code}")

logo = f"""{Fore.LIGHTRED_EX}
███╗   ███╗ ██████╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
████╗ ████║██╔════╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
██╔████╔██║██║     ██╔██╗ ██║███████║██╔████╔██║█████╗  
██║╚██╔╝██║██║     ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚═╝ ██║╚██████╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
"""

print(logo)

if len(sys.argv) < 2:
    print(Fore.RED + "This script must be run from the command line.\n")
    print(Fore.YELLOW + "python main.py <username>")
    input("")
    sys.exit()

username = sys.argv[1]
check_username(username)
input("\n")
