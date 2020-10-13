#This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
#
#You can start your Python journey anywhere, but to finish this exercise you will have to have finished 
# Parts 1 and 2 or use the solutions (Part 1 and Part 2).
#
#In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect 
# guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#
#In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing 
# the letter and displaying that information to the user. In this exercise, we have to put it all together and 
# add logic for handling guesses.
#
#Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
#    Only let the user guess 6 times, and tell the user how many guesses they have left.
#    Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize 
# them - let them guess again.
#
#Optional additions:
#
#    When the player wins or loses, let them start a new game.
#    Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. 
#      This is challenging - do the other parts of the exercise first!
#
#Your solution will be a lot cleaner if you make use of functions to help you!

def pickWord(dictFile):
    from random import choice
    with open(dictFile,'r') as dictFromFile:
        content = dictFromFile.readlines()
    return choice(content).strip()

def printHanfMan(failedAttempts):
    hangman = [
        '''         ------
         |    |
         |
         |
         |
         |
         ---------''',
         '''         ------
         |    |
         |    O
         |
         |
         |
         ---------''',
         '''         ------
         |    |
         |    O
         |    |
         |
         |
         ---------''',
         '''         ------
         |    |
         |    O
         |   /|
         |
         |
         ---------''',
         '''         ------
         |    |
         |    O
         |   /|\\
         |
         |
         ---------''',
         '''         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
         ---------''',
        '''         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
         ---------'''
    ]

    return hangman[failedAttempts]

def printBoard(word,dword,failedAttempts):
    board = ""
    for letter in word:
        board+="{0} ".format(dword[letter])
    print(printHanfMan(failedAttempts))
    print(board)

def userGuess():
    from string import ascii_lowercase

    while True:
        x = input("Give me a letter: ")
        if len(x) == 1:
            if x.lower() in ascii_lowercase:
                return x.upper()
            else:
                print("It must be a letter!")
        else:
            print("Just 1!")

if __name__ == "__main__":

    from os import system

    while True:
        word = pickWord('./30_pickWord.txt')
        dword = {}
        failedAttempts = 0
        attempts = 0

        for letter in word:
            dword[letter] = "_"

        while True:
            
            printBoard(word,dword,failedAttempts)
            x = userGuess()

            if x in word:
                system("clear")
                if dword[x] == '_':
                    attempts+=1
                    dword[x] = x
                else:
                    print("You already chose {0}. Try again!".format(x))
            else:
                system("clear")
                failedAttempts+=1
                print("{0} is not in the word! You have {1} guesses left!".format(x,6-failedAttempts))
            if "_" not in dword.values():
                printBoard(word,dword,failedAttempts)
                print("You have guessed the word! It took {0} guesses.".format(attempts+failedAttempts))
                break
            elif failedAttempts == 6:
                printBoard(word,dword,failedAttempts)
                print("You didn't guess! The word was: {0}".format(word))
                break

        while True:
            playAgain = input("Would you like to play again? (Yes/No): ")
            if playAgain.lower() != "yes" and playAgain.lower() != "no":
                print("Only valid options are 'Yes' and 'No'.")
            else:
                break
        if playAgain.lower() == "no":
            print("Thanks for playing!")
            break