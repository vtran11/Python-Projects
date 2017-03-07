
""" vtran
    The Goal: this project involves writing a program that simulates rolling dice.
    When the program runs, it will randomly choose a number between 1 and 6. 
    The program will print what that number is. It should then ask
    you if you would like to roll again.
"""


import random

#function to rolling a dice and return a side
def rand(sides=6):
    output = random.randint(1,sides)
    return output

#function to print out the result after rolling a dice
def main():
    print("Welcome to the Dice Rolling Simulator\n")
    cont = True
    while cont:
        interInput = raw_input("Q to quit or Enter any other key to Start Rolling a Dice:")

        if interInput.lower() != "q":
            out = rand(6)
            print("You rolled a %s" %(out))

        else:
            cont = False

    print("Thank you for using Dice Rolling Simulator!")
main()
