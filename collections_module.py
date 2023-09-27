# counter , namedtuple, Ordereddict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbbbbccccdddd"
mycounter = Counter(a)
print(mycounter)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(3))
print(mycounter.most_common(1)[0][0])

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# since python 3.7 dict can save the order of values
order_dict = OrderedDict()
order_dict["a"] = 1
order_dict["b"] = 2
order_dict["c"] = 3
order_dict["d"] = 4
order_dict["e"] = 5
print(order_dict)


d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
print(d["f"])

d = deque()
d.append(1)
d.append(3)
d.appendleft(5)
d.append(8)
d.pop()
print(d)
d.popleft()
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
