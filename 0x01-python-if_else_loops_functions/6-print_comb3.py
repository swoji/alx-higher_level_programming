#!/usr/bin/python3
for digit in range(0, 10):
    for digit1 in range(digit + 1, 10):
        if digit == 8 and digit1 == 9:
            print('{:d}{:d}'.format(digit, digit1))
        else:
            print('{:d}{:d}'.format(digit, digit1), end=', ')
