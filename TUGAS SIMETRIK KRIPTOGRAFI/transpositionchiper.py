import math

def encryptMessage(key, message):
    chiperText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            chiperText[col] += message[pointer]
            pointer += key
    return "".join(chiperText)

def decryptMessage(key, message):
    numCols = math.ceil(len(message)/key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0
    row = 0
    for symbol in message:
        plainText[col] += symbol
        col += 1
        if ((col == numCols) or (col == numCols-1) and (row >= numRows-numShadedBoxes)):
            col = 0
            row += 1
    return "".join(plainText)

message = input("Enter message: ")
key = int(input("Enter key [2-%s]: " % (len(message) - 1)))
mode = input("Encryption/Decryption [e/d]: ")
if mode.lower().startswith("e"):
    text = encryptMessage(key, message)
elif mode.lower().startswith("d"):
    text = decryptMessage(key, message)
print("Output:",text)
