from random import choice


def get_dna():
    yield "a"
    yield "c"
    while True:
        yield choice(["a", "c", "g", "t"])


# generator function
x = get_dna()
prev = None
# while True:
#     try:
#         val = next(x)
#         print(val, end=" ")
#         if val == "t" and prev == "g":
#             break
#         prev = val
#     except StopIteration:
#         break

while True:
    val = next(x)
    print(val, end=" ")
    if val == "t" and prev == "g":
        break
    prev = val
print()
# generator expression
prev = None
for i in get_dna():
    print(i, end=" ")
    if i == "t" and prev == "g":
        break
    prev = i
