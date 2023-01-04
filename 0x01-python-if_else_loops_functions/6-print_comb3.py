#!/usr/bin/python3

'''alx-higher_level_programming\Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical.
    '''
for digit in range(0, 10):
    for digit1 in range(digit + 1, 10):
        if digit == 8 and digit1 == 9:
            print('{:d}{:d}'.format(digit, digit1))
        else:
            print('{:d}{:d}'.format(digit, digit1), end=', ')
