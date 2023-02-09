def bubbleSort(arrayOfElements):
    arrayToReturn = arrayOfElements
    n = len(arrayToReturn)

    for i in range(0, n):

        #We must remeber that we have already check a few elements so no need to check that last bit.
        #We use i since j only represents a segment where i will always be the whole array
        for j in range(0,n-i-1):
            if(arrayToReturn[j] > arrayToReturn[j+1]):
                arrayToReturn[j], arrayToReturn[j+1] = arrayToReturn[j+1], arrayToReturn[j]
    return arrayToReturn


print("Please enter some numbers, type end to continue")

userInput = ""
userInputArray = []

while True:
    userInput = input()
    if userInput != "end":
        userInputArray.append(userInput)
    else:
        break


print("Here is the array before its sorted", end=" ")

for i in range(0, len(userInputArray)):
    print(str(userInputArray[i]), end=" ")

print("")

sortedArray = bubbleSort(userInputArray)

print("Here is the array after its sorted", end=" ")

for i in range(0, len(sortedArray)):
    print(str(sortedArray[i]), end=" ")

print("")