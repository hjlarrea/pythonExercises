#This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.
#
#In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:
#
#    Draw the Tic Tac Toe game board
#    Checking whether a game board has a winner
#    Handle a player move from user input
#
#The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in 
# this exercise is to use the functions from those previous exercises all together in the same program to make a two-
# player game that you can play with a friend. There are a lot of choices you will have to make when completing this 
# exercise, so you can go as far or as little as you want with it.
#
#Here are a few things to keep in mind:
#
#    You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
#    If there are no more moves left, don’t ask for the next player’s move!
#
#As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 
# or Player 2.

def printBoard(gameBoard):
    board = ""
    for i in range(0,3):
        for _ in range(0,3):
            board = board + " ---"
        board = board + "\n"
        for j in range(0,3):
            board = board + "| {0} ".format(gameBoard[i][j] if gameBoard[i][j] != 0 else " ")
        board = board + "|\n"
    for _ in range(0,3):
        board = board + " ---"
    print(board)

def checkIfWin(board):
    for i in range(0,len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board [i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board [2][i]:
            return board[i][0]
    if board[0][0] == board[1][1] and board[1][1] == board [2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board [2][0]:
        return board[0][2]
    else:
        return 0

def placeMovement(board,x,y,playerSymbol):
    if board[x][y] == 0:
        board[x][y] = playerSymbol
        return board
    else:
        raise NameError("Position Taken")

def getUserInput(playerNumber,playerSymbol,position):
    while True:
        try:
            y = int(input("Player {0} ({1}), please input the {2} for your movement: ".format(playerNumber,playerSymbol,position)))
            if y > 0 and y < 4:
                y-=1
                return y
            else:
                print("Value should be 1, 2 or 3.")
        except ValueError:
            print("Value is not a number.")

if __name__ == "__main__":

    players = {
        1: "X",
        2: "O"
    }

    wins = {
        1: 0,
        2: 0
    }

    while True:
        board = [[0,0,0],[0,0,0],[0,0,0]]

        for i in range (0,9):
            printBoard(board)
            while True:
                goesNext = 1 if i % 2 == 0 else 2
                x = getUserInput(goesNext,players[goesNext],"row")
                y = getUserInput(goesNext,players[goesNext],"column")

                try:
                    board = placeMovement(board,x,y,players[goesNext])
                    break
                except NameError:
                    print("Position is already taken. Try another one.")
            if i >= 4:
                if checkIfWin(board) != 0:
                    wins[goesNext]+=1
                    printBoard(board)
                    print("Player {0} won!".format(goesNext))
                    break
        while True:
            print("Player 1 won {0}, Player 2 won {1} times!".format(wins[1],wins[2]))
            playAgain = input("Do you want to play again? (Yes/No): ")
            if playAgain.lower() != 'yes' and playAgain.lower() != 'no':
                print("Only valid options are 'Yes' and 'No'.")
            else:
                break

        if playAgain.lower() == 'no':
                print("Thanks for playing!")
                break