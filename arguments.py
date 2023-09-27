# Default arguments
def sayhello(name="User"):
    print(f"Hello, {name}")


sayhello("Ayushi")


# Arbitary arguments
def sum_all(*nums):
    total = 0
    for i in nums:
        total += i


sum_all(1, 2, 3, 4)
sum_all(1, 2, 3)


# Positional Arguments Python
def add(a, b):
    return a + b


add(3, 4)
add(*(3, 4))


# keyword arguments python
def divide(a, b):
    return a / b


divide(3, 2)
divide(a=1, b=2)
divide(b=2, a=1)


# Python Arbitrary Arguments
def sayhello(*names):
    for name in names:
        print(f"Hello, {name}")


sayhello("Ayushi", "Leo", "Megha")
