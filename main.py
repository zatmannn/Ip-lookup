import requests
from pystyle import Colors, Write
import os

def ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        iptext = (f"""\n[+] > IP Adress: {response.get('ip', 'None')}
[+] > Сity: {response.get('city', 'None')} 
[+] > Region: {response.get('region', 'None')}
[+] > Country: {response.get('country', 'None')}
[+] > Postal code: {response.get('postal', 'None')}
[+] > ISP: {response.get('org', 'None')}
[+] > Latitude, longitude: {response.get('loc', 'None')}
[+] > Timezone: {response.get('timezone', 'None')}
[+] > Google Maps: https://www.google.com/maps?q={response.get('loc')}
""")
        Write.Print(iptext, Colors.blue_to_cyan, interval=0.0085)

    except requests.exceptions.Timeout:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n[!] > Request timed out. Please try again later.", Colors.red, interval = 0)
    except requests.exceptions.ConnectionError:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n[!] > Connection error.", Colors.red, interval = 0)
    except requests.exceptions.HTTPError as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print(f"\n[!] > HTTP error: {e.response.status_code}", Colors.red, interval = 0)
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print(f"\n[!] > An error occurred: {e}", Colors.red, interval = 0)

    Write.Input("\nPress Enter to return to the main menu...", Colors.blue_to_cyan, interval=0)
    os.system('cls' if os.name == 'nt' else 'clear')

def your_ip_info():
    url = "https://ipinfo.io/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        iptext = (f"""\n[+] > IP Address: {response.get('ip', 'None')}
[+] > City: {response.get('city', 'None')} 
[+] > Region: {response.get('region', 'None')}
[+] > Country: {response.get('country', 'None')}
[+] > Postal code: {response.get('postal', 'None')}
[+] > ISP: {response.get('org', 'None')}
[+] > Latitude, longitude: {response.get('loc', 'None')}
[+] > Timezone: {response.get('timezone', 'None')}
[+] > Google Maps: https://www.google.com/maps?q={response.get('loc')}
""")
        Write.Print(iptext, Colors.blue_to_cyan, interval=0.0085)

    except requests.exceptions.Timeout:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("[!] > Request timed out. Please try again later.", Colors.red, interval = 0)
    except requests.exceptions.ConnectionError:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("[!] > Connection error.", Colors.red, interval = 0)
    except requests.exceptions.HTTPError as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print(f"[!] > HTTP error: {e.response.status_code}", Colors.red, interval = 0)
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print(f"[!] > An error occurred: {e}", Colors.red, interval = 0)

    Write.Input("\nPress Enter to return to the main menu...", Colors.blue_to_cyan, interval=0)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        menu = """\n\n ██▓ ██▓███         ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██▒▓██░  ██▒      ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██▒▓██░ ██▓▒      ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░██░▒██▄█▓▒ ▒      ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░██░▒██▒ ░  ░      ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░▓  ▒▓▒░ ░  ░      ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
 ▒ ░░▒ ░           ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
 ▒ ░░░               ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
 ░                     ░  ░    ░ ░      ░ ░  ░  ░      ░              
\n\n╭─                  ─╮
│ [1] > IP info      │
│ [2] > Your IP info │
│ [3] > Exit         │
╰─                  ─╯
"""
        Write.Print(menu, Colors.blue_to_cyan, interval = 0)

        choice = Write.Input("[?] >  ", Colors.blue_to_cyan, interval = 0).strip()

        if choice == "1":
            ip = Write.Input("[?] > IP-Adress:", Colors.blue_to_cyan, interval = 0)
            if not ip:
                os.system('cls' if os.name == 'nt' else 'clear')
                Write.Print("[!] > Please, enter IP Adress\n", Colors.red, interval = 0)
                continue
            ip_info(ip)
        
        elif choice == "2":
            your_ip_info()

        elif choice == "3":
            Write.Print("\n[!] > Exiting...", Colors.blue_to_cyan, interval = 0)
            exit()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            Write.Print("[!] > Please, enter 1 or 2.\n", Colors.red, interval = 0)
            continue

main()