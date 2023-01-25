from getpass import getpass

userDbMap = {}

def initUser(username, password):
    userDbMap[username] = password

def readUserDb():
    userDbStream = open("userDb.txt", 'r')
    for user in userDbStream:
        userSplit = user.split()
        initUser(userSplit[0], userSplit[1])

readUserDb()

print("Please enter your username: ", end='')
usernameInput = input()
userpassInput = getpass()

if usernameInput in userDbMap:
    if userpassInput == userDbMap[usernameInput]:
        print("Welcome Commander")
    else:
        print("Incorrect Password. Exiting")
        exit(-1)
else:
    print("Incorrect username. Exiting")
    exit(-1)