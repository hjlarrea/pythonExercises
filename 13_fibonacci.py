#Write a program that asks the user how many Fibonnaci numbers to generate and 
# then generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
# sequence is the sum of the previous two numbers in the sequence. The sequence looks 
# like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib(limit):
    fibList = []
    for i in range(0,limit):
        if i == 0 or i == 1:
            fibList.append(1)
        else:
            fibList.append(fibList[-2]+fibList[-1])
    
    return fibList

limit = int(input("How many fibonacci numbers to print? "))
print(fib(limit))