my_info = ["Lenin", "Mishra", 28, "Amsterdam"]

name, surname, age, place = my_info

my_info = [("Lenin", "Mishra"), 28, "Amsterdam"]

name, age, place = my_info

my_info = ["Lenin", "Mishra", 28, "Amsterdam"]
# discard values while unpacking
name, surname, age, _ = my_info

my_info = {"name": "Lenin", "age": 28}

x, y = my_info

# Unpacking arbitrary length iterables
scores = [92, 90, 87, 64, 75, 91]
first, *middle, last = scores
