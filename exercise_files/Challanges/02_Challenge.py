# Python code​​​​​​‌​‌‌​​‌​​​​​​​‌‌​​​​‌​‌‌​ below

def factorial(num):
    # Your code goes here.
    if not type(num) is int or num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
number = 5
result = factorial(number)
print(result)
