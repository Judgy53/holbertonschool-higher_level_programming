#!/usr/bin/python3
upper = False
for i in range(26):
    print("{}".format(chr(ord('Z' if upper else 'z') - i)), end="")
    upper = not upper
