x = list(range(10))
print(x)

y = list(range(0, 100, 4))
print(y)

z = list(range(100, 0, -3))
print(z)


for i in range(len(z)):
    print(f"element{i}: {z[i]}")
