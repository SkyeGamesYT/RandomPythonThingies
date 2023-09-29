import sys
import time

#Credit to me, keep this in.
print('''
 ████ █   █  ███  █████ █████ █████ █   █ ████  █████ 
█     █   █ █   █ █       █     █    █ █  █   █ █     
█  ██ █████ █   █ █████   █     █     █   ████  ████  
█   █ █   █ █   █     █   █     █     █   █     █     
 ███  █   █  ███  █████   █     █     █   █     █████ 
𝗠𝗔𝗗𝗘 𝗕𝗬
SkyeGamesYT
https://github.com/SkyeGamesYT/RandomPythonThingies
''')


def ghost_type(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1) #Speed of typing
ghost_type("Test")
