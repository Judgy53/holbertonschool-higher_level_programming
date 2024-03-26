#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if len(out) == 0:
            out += str(i)
        print("{} ".format(out), end="")
