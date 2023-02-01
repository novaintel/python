morseCodeMapping = {"A": ".-", "B": "-...", "C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.",
"H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-",
"R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","0": "-----",
"1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----."}

def convertToMorse(string):
    morseCode = ""
    for char in string:
        morseCode += morseCodeMapping[char.upper()]
        morseCode += " "
    return morseCode

def convertFromMorse(string):
    splitText = string.split()
    humanText = ""

    for charCode in splitText:
        if charCode == '/':
            humanText += ' '
            continue
        humanText += list(morseCodeMapping.keys())[list(morseCodeMapping.values()).index(charCode)]

    return humanText

print(convertToMorse("Hello"))
print(convertFromMorse(".-- --- .-. .-.. -.."))

print(convertFromMorse(".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"))