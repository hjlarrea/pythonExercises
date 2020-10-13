#This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
#For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based 
# on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the 
# user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:
#
#>>> Welcome to the birthday dictionary. We know the birthdays of:
#Albert Einstein
#Benjamin Franklin
#Ada Lovelace
#>>> Who's birthday do you want to look up?
#Benjamin Franklin
#>>> Benjamin Franklin's birthday is 01/17/1706.
#
#Happy coding!

if __name__ == "__main__":
    birthdays = {
        "Pedro": "23/12/1986",
        "Pablo": "25/08/1986",
        "Ana": "21/05/1984"
    }

    print("Welcome to the birthday dictionary. We know the birthdays of: \n{0}".format('\n'.join(birthdays.keys())))

    while True:
        name = input("Who's birthday do you want to look up? ")
        if name not in birthdays.keys():
            print("Input a valid name from the known names.")
        else:
            break
    
    print("{0}'s birthday is on {1}".format(name,birthdays[name]))