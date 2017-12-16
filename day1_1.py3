#!/usr/bin/env python

import sys

if sys.argv:
    try:
        raw = input('Puzzle input:')
        puzzle_input = int(raw)
    except ValueError:
        print("Puzzle input needs to be a number")
        exit()
else:
    puzzle_input=sys.argv[1]

last_digit = str(puzzle_input)[-1]
total = 0

for digit in str(puzzle_input):
    if digit==last_digit:
        print("Last digit was: "+last_digit+", match found")
        total+=int(digit)
        print("Total is now "+str(total))
    last_digit=digit

print(total)
