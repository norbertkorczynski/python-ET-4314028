# Python code​​​​​​‌​‌‌​​‌​​​‌‌​​‌‌‌​‌​​‌‌​‌ below
import json
import os

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        if(len(item)) >= 2:
            print(item)
            print(len(item))
            decodedStr = decodedStr + item[0] * item[1]
        else:
            decodedStr = decodedStr + item
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    with open(filename, 'r') as input:
        with open(newFilename, 'w') as output:
            output.writelines([ch + str(count) for ch, count in encodeString(input.readlines())])
            output.close()

def decodeFile(filename):
    # Your code also goes here.
    lines = []
    with open(filename, 'r') as input:
        lines = input.readlines()
    return decodeString(lines)
    



original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
Answer.encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

new_filesize = os.path.getsize("10_04_challenge_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = Answer.decodeFile('10_04_challenge_art_encoded.txt')
print(decoded)