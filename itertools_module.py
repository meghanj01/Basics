# itertools : product , permutation, combinations, accumulate, groupby

from itertools import (
    count,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
)
import operator

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
prod = product(a, b, repeat=2)
print(list(prod))

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(a))

a = [1, 2, 3, 4]
com = combinations(a, 2)
print(list(com))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(list(acc))


def smaller_than_3(x):
    return x <= 3


a = [1, 2, 3, 5]
group_obj = groupby(a, key=smaller_than_3)
group_obj = groupby(a, key=lambda x: x < 3)
for key, val in group_obj:
    print(key, list(val))
