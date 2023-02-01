for i in range(99, 0, -1):
    if i > 2:
        print(str(i) + " bottles of beer on the wall Take one down and pass it around, " + str(i-1) + " bottles of beer on the wall.", end=" ")
    elif i == 2:
        print(str(i) + " bottles of beer on the wall Take one down and pass it around, 1 bottle of beer on the wall.", end=" ")
    elif i == 1:
        print(str(i) + " bottle of beer on the wall Take one down and pass it around, no more bottles of beer on the wall.", end=" ")

print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")       