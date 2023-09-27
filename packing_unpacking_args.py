# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)


# A Python program to demonstrate use
# of packing


# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    return sum(args)


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
    print(a, b, c)


# A call with unpacking of dictionary
d = {"a": 2, "b": 4, "c": 10}
fun(**d)


# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))


# Driver code
fun(name="geeks", ID="101", language="Python")
