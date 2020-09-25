# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
# makes a new list of only the first and last elements of the given list. For practice, 
# write this code inside a function.

from random import randint

def sliceList(myList):
    result = []
    result.append(myList[0])
    result.append(myList[-1])
    return result

myList = []

for i in range(0,randint(1,99)):
    myList.append(randint(1,99))

print("Generated list:")
print(myList)
print("Filtered list:")
print(sliceList(myList))