a_list = [2, 3, 4, 5, 6, 7, None]
tup = ("f", "bar", "baz")
b_list = list(tup)
print(b_list)
print(b_list[1])
b_list[1] = "peekabo"
print(b_list)

# Ading and removint elements
b_list.append("add")
print(b_list)
b_list.insert(1, "xd")
print(b_list)
b_list.pop(2)
print(b_list)
