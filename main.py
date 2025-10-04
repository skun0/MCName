import requests
from colorama import Fore
import os

while True:
    logo = '''
    ███╗   ███╗ ██████╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
    ████╗ ████║██╔════╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
    ██╔████╔██║██║     ██╔██╗ ██║███████║██╔████╔██║█████╗  
    ██║╚██╔╝██║██║     ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
    ██║ ╚═╝ ██║╚██████╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                                                        '''
    print(Fore.CYAN + logo)

    
    username = input(Fore.RESET+"$")
    if not username.strip():
        continue

    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            print(f"{username} is taken")
        except Exception:
            print("Error")
    elif r.status_code in (204, 404):
        print(f"{username} is NOT taken")
    else:
        print(f"{r.status_code}")

    os.system("pause")
