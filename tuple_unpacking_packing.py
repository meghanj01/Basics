# Python3 code to study about
# unpacking python tuple using *

# first and last will be assigned to x and z
# remaining will be assigned to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

# print details
print(x)
print(y)
print(z)

# first and second will be assigned to x and y
# remaining will be assigned to z
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)
print(x)
print(y)
print(z)


# Python3 code to study about
# unpacking python tuple using function


# function takes normal arguments
# and multiply them
def result(x, y):
    return x * y


# function with normal variables
print(result(10, 100))

# A tuple is created
z = (10, 100)

# Tuple is passed
# function unpacked them

print(result(*z))
