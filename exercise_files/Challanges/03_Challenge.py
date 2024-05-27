# Python code​​​​​​‌​‌‌​​‌​​​‌​​​​‌‌​​‌​​​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if not isinstance(hexNum, str):
        return None
    result = 0
    multiplicator = 1
    print(hexNum)
    for h in hexNum[::-1]:
        decimal = hexNumbers.get(h)
        print(f'h({h}) = {decimal}')
        if not decimal is None:
            result = result + decimal * multiplicator
        else:
            return None
        multiplicator = multiplicator * 16
    return result



# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

print(hexToDec('0'))
print(hexToDec('GGG'))
print(hexToDec('A2'))
print(hexToDec('spam spam spam'))
