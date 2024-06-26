#!/usr/bin/python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["mango", "orange", "lemon", "coconut", "pineaple"]
for i in x:
    print(i)
for i in range(len(y)):
    print(y[i])

[print(i) for i in x]

z = [i for i in y if i != 'lemon']
print(z)
k = [y[i] for i in range(len(y))]
print(k)

for i in x:
    if i > 5:
        print(i)
    else:
        print(f"{i} is not greater than 5")
j = [i if i != "mango" else "orange" for i in y]
print(j)

unsorted = [4, 3, 2, 0, 1, 9, 8, 7]
j = sorted(unsorted)
print(unsorted)


m = x.copy()
print("Before changing", m)
x[5] = 12
print("After changing", m)
print()
print()
# ----------- Tuple ---------------
t = ("apple", "banana", "cherry")
print(t)
myTuple = ("mango",)
print(type(t))
newList = list(t)
newList[1] = "mango"
t = tuple(newList)
print(t)
(m, *n) = t
print(m)
print(n)
s = 0
while s < len(t):
    print(t[s])
    s = s + 1

o = t * 2
print(o)

