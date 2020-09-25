#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use 
# the user input lessons from the very first exercise)
#
#Extras:
#
#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends, print this out.


from random import randint
continuePlaying = True
matches = {
    "plays": 0,
    "wins": 0
}

while continuePlaying:
    guessMe = randint(1,9)

    userInput = input("Guess which number between 1 and 9 has the computer generated (or 'exit' to stop playing): ")
    
    if userInput.lower() == "exit":
        continuePlaying = False
        print("Played {0} matches, won {1}!".format(matches["plays"],matches["wins"]))
    else:
        userGuess = int(userInput)
        matches["plays"] += 1

    if continuePlaying:
        if userGuess == guessMe:
            matches["wins"] += 1
            print("Well done! The computer generated number was {0}".format(guessMe))
        elif userGuess > guessMe:
            print("Too high! It was: {0}".format(guessMe))
        elif userGuess < guessMe:
            print("Too low! It was: {0}".format(guessMe))