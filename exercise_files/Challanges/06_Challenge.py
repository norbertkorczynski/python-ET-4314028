# Python code​​​​​​‌​‌‌​​‌​​​‌​‌‌​​​‌​‌​‌‌‌‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num-1)


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

print(square(9))
