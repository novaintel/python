from random import *

def generateCharacter():
    asciiInt = randint(33,122)
    asciiChar = chr(asciiInt)
    return asciiChar

def genPassword(length):
    password = ""
    for j in range(length):
        password += generateCharacter()
    return password

def writeToFile(text):
    f = open("Passwords.txt", "a")
    f.write(text)
    f.write("\n")
    f.close

print("How many passwords do you wish to generate?")
numPasswords = int(input())
print("Please enter the length of the password you want")
length = int(input())
#This is super risky but I trust myself
for i in range(numPasswords):
    writeToFile(genPassword(length))
