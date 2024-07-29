#!/usr/bin/python

import os

#f = open("example.txt", "w")
#x = open("../../password.txt", "at")
#print(f.read())
#f.write("Now i have added a new content to our file")
#f.close()
#print(x.read())
#print(x.read().split(" "))
#print(x.readline())
#x.write("Admin123456")
#x.close()

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("The file you want to delete does not exist")

