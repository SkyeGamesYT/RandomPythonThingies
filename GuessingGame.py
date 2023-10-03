'''
SkyeGamesYT
10/3/23
GuessingGame.py
This program generates a random number, and has user guess it through input.
'''
import os
import colorama
import random
from colorama import Fore, Style


#Clear message when run
os.system("clear")
#Start
#Credit, keep this in please.
print(f'''{Fore.YELLOW}

 ████ █   █ █████ █████ █████   ████  ███  █   █ █████ 
█     █   █ █     █     █      █     █   █ ██ ██ █     
█  ██ █   █ ████  █████ █████  █  ██ █████ █ █ █ ████  
█   █ █   █ █         █     █  █   █ █   █ █   █ █     
 ███  █████ █████ █████ █████   ███  █   █ █   █ █████ 
𝗠𝗔𝗗𝗘 𝗕𝗬
SkyeGamesYT
https://github.com/SkyeGamesYT/RandomPythonThingies




{Style.RESET_ALL}''')
guess = int(input()
answer = random.randrange(11) #0-10 are options.

print(f"{Fore.CYAN}Guess a Number!{Style.RESET_ALL}")

if guess == answer:
  print(f"{Fore.GREEN}You got it! The answer was{Style.RESET_ALL}", answer)
else:
  print(f"{Fore.RED}Wrong! Thw answer was{Style.RESET_ALL}", answer)
