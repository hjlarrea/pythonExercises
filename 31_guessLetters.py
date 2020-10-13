#This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
#
#Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the 
# player has to guess, letter by letter. The player guesses one letter at a time until the entire word 
# has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
#
#Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks 
# a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, 
# let the player guess an infinite number of times until they get the entire word. As a bonus, keep track 
# of the letters the player guessed and display a different message if the player tries to guess that 
# letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry 
# about choosing a word randomly or keeping track of the number of guesses the player has remaining - we 
# will deal with those in a future exercise.
#
#An example interaction can look like this:
#
#>>> Welcome to Hangman!
#_ _ _ _ _ _ _ _ _
#>>> Guess your letter: S
#Incorrect!
#>>> Guess your letter: E
#E _ _ _ _ _ _ _ E
#...
#
#And so on, until the player gets the word.

def pickWord(dictFile):
    from random import choice

    with open(dictFile,'r') as dictFromFile:
        content = dictFromFile.readlines()

    return choice(content).strip()

def printBoard(word,dword):
    board = ""
    for letter in word:
        board+="{0} ".format(dword[letter])
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
    
    word = pickWord('./30_pickWord.txt')
    dword = {}
    attempts = 0

    for letter in word:
        dword[letter] = "_"

    while True:
        printBoard(word,dword)
        x = userGuess()
        attempts+=1
        if x in word:
            dword[x] = x
        if "_" not in dword.values():
            printBoard(word,dword)
            print("You have guessed the word! It took {0} guesses.".format(attempts))
            break