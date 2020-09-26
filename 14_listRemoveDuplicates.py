#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
#Extras:
#
#    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#    Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def removeDuplicates(myList):
    newList = []
    duplicates = []
    for i in range(0,len(myList)):
        occurences = 0
        for j in range(0,len(myList)):
            if myList[i] == myList[j]:
                occurences += 1
        if occurences == 1:
            newList.append(myList[i])
        elif myList[i] not in duplicates:
            duplicates.append(myList[i])
    return newList + duplicates

def removeDuplicates2(myList):
    newList = []
    for i in range(0,len(myList)):
        if myList[i] not in newList:
            newList.append(myList[i])
    return newList

def removeDuplicates3(myList):
    return list(set(myList))

from random import randint

#### MAIN #####

myList = []
listLen = randint(1,50)

for i in range(0,listLen):
    myList.append(randint(1,99))

print("Generated list: {0}".format(myList))
print("Without duplicates: {0}".format(removeDuplicates(myList)))
print("Without duplicates: {0}".format(removeDuplicates2(myList)))
print("Without duplicates: {0}".format(removeDuplicates3(myList)))
