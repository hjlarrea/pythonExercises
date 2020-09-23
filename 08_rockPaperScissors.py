#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the 
# players want to start a new game)
#
#Remember the rules:
#
#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock
#

def player(playerName):
    while True:
        try:
            player = int(input("{0} Chose 1 for Rock, 2 for Paper or 3 for Scissors: ".format(playerName)))
            if player in [1,2,3]:
                break
            else:
                print("Only valid options are 1,2 or 3.")
        except ValueError:
            print("Only valid options are 1,2 or 3.")
    return player

playAgain = True

while playAgain:
    player1 = player("Player 1")
    player2 = player("Player 2")
    if (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 ==1):
        print("Player 1 wins.")
    elif player1 == player2:
        print("Tie!")
    else:
        print("Player 2 wins.")
    
    while True:
        userOption = input("Would you like to play again? (Yes/No)")
        if userOption == "No":
            playAgain = False
            break
        elif userOption == "Yes":
            break
        elif userOption != "Yes" and userOption != "No":
            print("Only possible options are 'Yes' or 'No'")