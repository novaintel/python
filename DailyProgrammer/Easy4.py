from random import *

def generateCharacter():
    asciiInt = randint(33,122)
    asciiChar = chr(asciiInt)
    print("I gen this char: " + asciiChar)
    return asciiChar

def genPassword(length):
    password = ""
    for i in range(length):
        password += generateCharacter()
    return password

print("Please enter the length of the password you want")
length = input()
#This is super risky but I trust myself
genPassword = genPassword(int(length))
print("The password we have generated is: " + genPassword)