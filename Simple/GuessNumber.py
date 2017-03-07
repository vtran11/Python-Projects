""" vtran
 The Goal: this project also uses the random module in Python. The program will first 
 randomly generate a number unknown to the user. The user needs to guess what that
 number is. If the users guess is wrong, the program should return some sort of indication as
 to how wrong(The number is too high or too low).  If the user guesses correctly, 
 a positive indication should appear. You will need functions to check if the user
 input is an actual number, to see the difference between the inputted number and 
 the randomly generated numbers, and to then compare the numbers.
"""

import random

def main():
    print("Welcome to the Guess Game!")
    randomNum = random.randint(1,50)
    guess = True
    guessCount = 1;
    
    input = int(raw_input("Guess a number between 1 and 50: "))
    
    while guess:
        if input>50:
            input = int(raw_input("The input is too high! \nGuess a number between 1 and 50:  "))
            guessCount +=1;
        elif input<1:
            input = int(raw_input("The input is too low! \nGuess a number between 1 and 50:  "))
            guessCount +=1;

        elif input == randomNum:
                print("You are correct!!!\n")
                guess = False
        else:
            input = int(raw_input("The input is incorrect! \nGuess a number between 1 and 50:  "))
            guessCount +=1;
        
        if guessCount == 10:
            print("You guessed 10 times with incorrect numbers! GAME OVER. ")
            guess = False
    
    print("Thanks for playing this game!")
main()
