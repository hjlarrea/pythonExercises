#Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this 
# opportunity to practice using functions, described below.

def howManyDivisors(num):
    divisors = 0
    for i in range(1,num+1):
        if num%i == 0:
            divisors+=1

    return divisors

userNumber = int(input("Give me a number: "))

if howManyDivisors(userNumber) == 2:
    print("{0} is prime!".format(userNumber))
else:
    print("{0} is not prime!".format(userNumber))