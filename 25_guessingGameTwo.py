#In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#
#This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 
# 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
#At the end of this exchange, your program should print out how many guesses it took to get your number.
#
#As the writer of this program, you will have to choose how your program will strategically guess. A naive 
# strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle 
# of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find 
# the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)


if __name__ == "__main__":
    print("Think a number between 0 and a 100. I'll try to guess which one it is!")
    guesses = 0
    i = 0
    k = 100
    j = int((k-i)/2)
    while True:
        guesses+=1
        answer = input("Is it {0}? (Yes / Higher / Lower): ".format(j))
        if answer.lower() != "yes" and answer.lower() != "higer" and answer.lower() != "lower":
            print("Answer should be 'Yes', 'Higer' or 'Lower'.")
        elif answer.lower() == "yes":
            print("Guessed! I tried {0} times before guessing.".format(guesses))
            break
        elif i == j or k == j:
            print("Somehow I didn't guess, are you sure you are not cheating?")
            break
        elif answer.lower() == "higer":
            i=j
            j=int((k-i)/2)+i
        elif answer.lower() == "lower":
            k=j
            j=int((k-i)/2)+i
            