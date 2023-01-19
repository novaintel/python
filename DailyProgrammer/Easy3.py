# (str(opt(c) + 2))

def encodeMessage(message, code):
    result = ""
    for element in message:
        result += chr(ord(element) + code)
    return result

def decodeMessage(message, code):
    result = ""
    for element in message:
        result += chr(ord(element) - code)
    print(result)

encodeMessage = encodeMessage("Hello World", 2)
decodeMessage(encodeMessage, 2)