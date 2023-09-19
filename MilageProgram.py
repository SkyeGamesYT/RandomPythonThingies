'''
Name Here
9/19/23
MilageProgram.py
This program is for determining Milage per car.


Variables
Var Name - Var Desc.

carName - Name of car (User Input)
titleCarName - Title vers. of carName
tankSize - Tank size of car.
milesPerGallon - How many miles/gallon the car can drive
costPerGallon - Cost of a gallon.
'''
import colorama #Coloring Made Easier.
from colorama import Fore, Style #Once again, coloring made easier.


#Welcome
print("Welcome to the Milage Program!")
print("This program will help you determine the milage on your car!")
print("\n\n\n")


#Body
carName = input("What type of car did you get? \n")
print("\n")
titleCarName = carName.title()
tankSize = float(input("What is the tank size of your", titleCarName, "? \n"))
print("\n")
milesPerGallon = float(input("How many miles can your", titleCarName, "go on one gallon? \n"))
print("\n")
costPerGallon = float(input("What is the cost for a gallon of gas? \n"))
print("\n\n\n")
wait(0.3)
print(Fore.RED"Calculating...")
wait(0.5)
#Math



