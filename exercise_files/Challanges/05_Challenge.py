# Python code​​​​​​‌​‌‌​​‌​​​‌​‌​‌‌​‌​‌​​‌​​ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    # Your code goes here.
    primesFound = []
    for n in range(3,num,2):
        for p in primesFound:
            if n % p == 0:
                break
        else:
            primesFound.append(n)
    primesFound.insert(0,2)
    return primesFound


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.

num = 100
result = allPrimesUpTo(num)
print(result)
