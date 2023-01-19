def toString(arrayToConvert):
    stringResult = ""
    for i in range(len(arrayToConvert)):
        if i == len(arrayToConvert) - 1:
            stringResult += ' and '
        
        stringResult += arrayToConvert[i]

        if i < len(arrayToConvert) - 2:
            stringResult += ', '

    return stringResult

spam = ['apples', 'bananas', 'tofu', 'cats']

print(toString(spam))

spam2 = ['1', '2', '3', '4', '5', '6', '7', '8']

print(toString(spam2))

spam3 = ['one', 'two']

print(toString(spam3))
