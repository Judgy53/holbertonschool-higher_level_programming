#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigit = abs(number) % 10
if number < 0:
    lastDigit *= -1

out = f'Last digit of {number} is {lastDigit} and is '
if lastDigit > 5:
    print(out + 'greater than 5')
elif lastDigit == 0:
    print(out + '0')
else:
    print(out + 'less than 6 and not 0')
