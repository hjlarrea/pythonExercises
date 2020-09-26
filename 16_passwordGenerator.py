# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of 
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password 
# every time the user asks for a new password. Include your run-time code in a main method.
#
#Extra:
#
#    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def generateStrongPassword(length):
    import string
    from random import randint

    charCollection = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ""

    for _ in range(0,length):
        password += charCollection[randint(0,len(charCollection))]

    return password

def generateWeakPassword():
    from random import randint

    with open('./palabras_todas.txt') as fileContent:
        content = fileContent.readlines()

    return content[randint(0,len(content))].split("\n")[0]+content[randint(0,len(content))].split("\n")[0]

def generatePassword(passType):
    complexLength = 30

    if passType.lower() == "weak":
        return generateWeakPassword()
    else:
        return generateStrongPassword(complexLength)

correctPassType = False

while not correctPassType:
    passType = input("Paassword type (weak/strong): ")
    if passType.lower() == "weak" or passType.lower() == "strong":
        correctPassType = True
    else:
        print("Only 'weak' or 'strong' are valid options.")

print(generatePassword(passType.lower()))