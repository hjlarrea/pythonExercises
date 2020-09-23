#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

myString = input("Input your string: ")
isPalindrome = True

for i in range(0,len(myString)):
    if myString[i] != myString[(i+1)*-1]:
        isPalindrome = False
        break

if isPalindrome:
    print("The word {0} is a palindrome.".format(myString))
else:
    print("The word {0} is not a palindrome.".format(myString))