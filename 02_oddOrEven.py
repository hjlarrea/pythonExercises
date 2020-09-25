#Exercise 2
#
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#
#    If the number is a multiple of 4, print out a different message.
#    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number1 = int(input("Input a number: "))
number2 = int(input("Input a second number: "))

if number1 % 4 == 0:
    print("{0} is divisible by 4, therefore is even.".format(number1))
elif number1 % 2 == 0:
    print("{0} is divisible by 2, therefore is even.".format(number1))
else:
    print("{0} is odd.".format(number1))

if number1 % number2 == 0:
    print("{0} is divisible by {1}.".format(number1,number2))
else:
    print("{0} is not divisible by {1}.".format(number1,number2))

