#Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
#
#The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

def maxOfThree(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c

if __name__ == "__main__":
    value1 = input("Value 1: ")
    value2 = input("Value 2: ")
    value3 = input("Value 3: ")
    maxValue = maxOfThree(value1,value2,value3)
    print("Maximum value was: {0}".format(maxValue))