import colorama
from colorama import Fore, Style


print(f"{Fore.MAGENTA}-{Style.RESET_ALL}"*50)
print("\n")
#Credit, leave this in.
print(f'''
{Fore.RED}
█   █ █   █ █     █████ █████ █   █ █████ █   █ █   █ 
██ ██ █   █ █       █     █   ██ ██ █     ██  █ █   █ 
█ █ █ █   █ █       █     █   █ █ █ ████  █ █ █ █   █ 
█   █ █   █ █       █     █   █   █ █     █  ██ █   █ 
█   █ █████ █████   █   █████ █   █ █████ █   █ █████ 
𝗠𝗔𝗗𝗘 𝗕𝗬
SkyeGamesYT
https://github.com/SkyeGamesYT/RandomPythonThingies



{Style.RESET_ALL}''')
print("\n\n\n")
print('''
𝗖𝗛𝗢𝗜𝗖𝗘𝗦

1. Choice 1
2. Choice 2
3. Choice 3



''')

choice = input("Please Make a choice: ")
if choice == "1":
  print("Choice 1 code")
elif choice == "2":
  print("Choice 2 code")
elif choice == "3":
  print("Choice 3 code")
#Add more by following format.
choice = input(f"{Fore.GREEN}Make your choice here: {Style.RESET_ALL}")
