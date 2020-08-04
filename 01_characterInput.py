#Exercise 1
#
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#
#    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input("Input your name: ")
age = int(input("Input your age: "))
times = int(input("How many times you want to print the message? "))

willTurn100In = datetime.date.today().year + 100 - age

for num in range(0,times):
    print("{0}, you'll turn 100 in {1}".format(name,willTurn100In))
