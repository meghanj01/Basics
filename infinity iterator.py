#  infinite iterators
from itertools import count, cycle, repeat


for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break


for i in repeat(1, 4):
    print(i)
