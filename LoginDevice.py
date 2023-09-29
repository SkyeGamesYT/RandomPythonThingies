import os
import colorama
from colorama import Fore, Style
#Gets rid of message at start in replit
os.system("clear")
#Keep this in, credit to me
print(f'''{Fore.MAGENTA}
█      ███   ████ █████ █   █ █████ █   █ █████ █████ █████ █   █ 
█     █   █ █       █   ██  █ █      █ █  █       █   █     ██ ██ 
█     █   █ █  ██   █   █ █ █ █████   █   █████   █   ████  █ █ █ 
█     █   █ █   █   █   █  ██     █   █       █   █   █     █   █ 
█████  ███   ███  █████ █   █ █████   █   █████   █   █████ █   █ 

𝗠𝗔𝗗𝗘 𝗕𝗬
SkyeGamesYT
https://github.com/SkyeGamesYT/RandomPythonThingies

{Style.RESET_ALL}
''')


#Username & Pass. Customizable
user = "example"
password = "example"


usercheck = input(f"{Fore.CYAN}Username: {Style.RESET_ALL}")
passcheck = input(f"{Fore.CYAN}Password: {Style.RESET_ALL}")

if user == usercheck and password == passcheck:
  print(f"{Fore.GREEN}Access Granted.{Style.RESET_ALL}")
  ##Code goes here
else:
  print(f"{Fore.RED}Access Denied.{Style.RESET_ALL}")
