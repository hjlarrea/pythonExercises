#Exercise 5
#Take two lists, say for example these two:
#
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.
#
#Extras:
#
#    Randomly generate two lists to test this
#    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

from random import randint 

list1 = []
list2 = []
list1Len = randint(0,20)
list2Len = randint(0,20)

for i in range(0,list1Len):
    list1.append(randint(0,100))

for i in range(0,list2Len):
    list2.append(randint(0,100))

returnList = list(set(list1).intersection(set(list2)))
print("List 1: {0}".format(list1))
print("List 2: {0}".format(list2))
print("Intersection: {0}".format(returnList))