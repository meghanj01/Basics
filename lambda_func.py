# mostly used in sorted, reduce , map, filter
add_val = lambda x: x + 10
print(add_val(5))

add_two = lambda x, y: x + y
print(add_two(2, 3))

points2D = [(1, 8), (1, 9), (3, 4), (5, 6)]
points2D = sorted(points2D, key=lambda x: x[1])
print(points2D)
