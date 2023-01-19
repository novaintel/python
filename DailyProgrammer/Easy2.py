# Calculate F = M * A
# Calculate A = F / M
# Calculate M = F / A

def calculateForce():
    print("Please enter the mass")
    mass = input()
    print("Please enter the Accleration")
    acclertation = input()
    force = int(mass) * int(acclertation)
    print("The force is: " + str(force))

def calculateAccleration():
    print("Please enter the force")
    force = input()
    print("Please enter the mass")
    mass = input()
    accleration = int(force) / int(mass)
    print("The accleration is: " + str(accleration))

def calculateMass():
    print("Please enter the force")
    force = input()
    print("Please enter the accleration")
    accleration = input()
    mass = int(force) / int(accleration)
    print("The mass is: " + str(mass))

operation = ""
while input != "quit":
    print("Please enter a thing you wish to calculate, M for Mass, F for force and A for acceleration")
    operation = input()
    if operation == "A":
        calculateAccleration()
    elif operation == "M":
        calculateMass()
    elif operation == "F":
        calculateForce()
    elif operation == "quit":
        break
