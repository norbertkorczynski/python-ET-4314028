# Python code​​​​​​‌​‌‌​​‌​​​‌​‌‌‌​‌‌‌‌​​​‌‌ below
def handleNonIntArguments(func):
    def wrapper(*args):
        for a in args:
            if type(a) is not int:
                raise NonIntArgumentException
        return func(*args)
    return wrapper


class NonIntArgumentException(Exception):
    pass


# This is how your code will be called.
# Your answer should be the largest value in the numbers list.
# You can edit this code to try different testing cases.

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')
