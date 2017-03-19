
"""vtran
    The Goal: Create a sort of "guess the word" game.
    The user need to be able to input letter guesses (set a LIMIT of guess number).
    Need a function to check if the user has actually input a single letter, to check if
    the inputted letter is in the hidden word and how many times it appear, to print letters
    and a counter variable to limit guesses.
    """

import random

def word_list():
    word = ["Little", "Sunflower", "Pungee", "Cat", "Hangman", "MadLid", "masterpiece",
            "compose", "eartwicked", "doubltful", "incapable", "glamorous", "Naibigan",
            "glossary", "enthusiasm", "preposterous", "enthusiastic", "notwithstanding",
            "flabbergasted", "thwarted", "exquisite", "shenanigans", "unjustifiable",
            "sensuality", "serendipity", "humongous", "shenanigans", "statuesque"]
            
    return random.choice(word).upper()

def check(word, guess, guessList):
    matches = 0
    output = ""
    
    for letter in word:
        if letter in guessList:
            output += letter
            matches+=1
        else:
            output+='*'

    if matches >= 1:
        print("Great! Your guess appears {} time(s) in the word!".format(matches))
    else:
        print("Oop!!Your guess is incorrect!")

    return output

def main():
    guessList = []
    word = word_list() #get the word
    
    print("Welcome to the Hangman game!!!")
    print("The word have {} letters".format(len(word)))
    
    
    for index in range(1,21):
        list = "Enter your guess (1 letter or a {}-letter word): ".format(len(word))
        guess = raw_input(list)
        guess = guess.upper()
        
        if len(guess) is 1:
            guessList.append(guess)
            checkWord = check(word, guess, guessList)
            print(checkWord)
            if checkWord == word.upper():
                print("Yes!!!You are correct! The word is {}".format(word))
                return
    
        elif len(guess) is len(word):
            if guess == word.upper():
                print("Yes!!!You are correct! The word is {}".format(word))
                return
            else:
                print("Your guess should be 1 letter or a {}-letter word):".format(len(word)))
        else:
            print("Invalid input!")
                        

    print("You can not guess the word after 20 tries!!Game Over.")
main()
