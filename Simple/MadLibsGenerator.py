
"""
 The program will first prompt the user for a series of inputs a la Mad Libs. 
 For example, a singular noun, an adjective, etc. Then, once all the information 
 has been inputted, the program will take that data and place them into a premade
 story template. You will need prompts for user input, and to then print out the
 full story at the end with the input included.
 """

story = '''He said stupidly as he {} into his convertible
{} next to the {} and drove off with his {} and {} wife.'''


def main():
    verb = raw_input("Enter a past tense verb: ")
    animal = raw_input("Enter an animal: ")
    noun = raw_input("Enter a noun: ")

    adjectives = []
    adjectives.append(raw_input("Enter an adjective:" ))
    adjectives.append(raw_input("Enter another adjective:" ))

    madLibs = story.format(verb, animal, noun, adjectives[0], adjectives[1])
    
    print(madLibs)

main()
