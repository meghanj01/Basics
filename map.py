def mul(i):
    return i * i


x = list(map(mul, (3, 4, 5, 6, 7)))
print(x)


example = ["Welcome", "to", "Simplilearn"]

x = list(map(len, example))

print(x)


import math

num = [9, 36, 49, 81, 121]

x = list(map(math.sqrt, num))

print(x)
