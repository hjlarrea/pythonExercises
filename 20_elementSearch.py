#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) an 
# appropriate boolean.
#
#Extras:
#
#    Use binary search.

if __name__ == "__main__":
    from random import randint

    myList = []

    for _ in range(0,randint(0,99)):
        myList.append(randint(0,99))

    myList = list(set(myList))
    myNum = randint(0,99)

    i = 0
    k = len(myList)-1
    j = int((k-i)/2)+i

    while True:
        if myNum == myList[j]:
            print("Found {0} in position:{1}\n{2}".format(myNum,j,myList))
            break
        elif i == j or j == k:
            print("{0} not found in:\n{1}".format(myNum,myList))
            break
        elif myNum > myList[j]:
            i = j
            j = int((k-i)/2)+i
        elif myNum < myList[j]:
            k = j
            j = int((k-i)/2)+i