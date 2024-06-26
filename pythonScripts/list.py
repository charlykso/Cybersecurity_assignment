#!/usr/bin/python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["banana", "apple", "mango", "guava", "pawpaw"]

print(len(x))
print(len(y))
print(type(x))
print(type(y))

print(x[1:4])
print(y[:3])
print(y[2:])
print(y[-2])
print("mango" in y)
if "lemon" not in y:
    print("Lemon is not in the list y")

l = len(y)
y[1:2] = ["lemon", "orange"]
print(y)
if "lemon" in y:
    print("Lemon is in the list y")

x.insert(2, 10)
print(x)
x.remove(10)
print(x)

for i in x:
    print(i)

for i in range(len(y)):
    print(y[i])

j = 0
while j <= len(x) - 1:
    print(x[j])
    j += 1

[print(k) for k in y]

