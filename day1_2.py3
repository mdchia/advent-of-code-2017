#!/usr/bin/env python

import sys

if sys.argv:
    try:
        raw = input('Puzzle input:')
        puzzle_input = int(raw)
    except ValueError:
        print("Puzzle input needs to be a number")
        exit
else:
    puzzle_input=sys.argv[1]

def shift_string(s, n):
    new = s[-n:]+s[:-n]
    return new

puzzle_input=str(puzzle_input)
jump_dist=len(puzzle_input)//2

shifted = shift_string(puzzle_input, jump_dist)
#print(shifted)
#print(jump_dist)

total = 0

for i in range(len(puzzle_input)):
    if puzzle_input[i]==shifted[i]:
        print("Match at position "+str(i)+" ("+puzzle_input[i]+")")
        total+=int(puzzle_input[i])
        print("Total is now "+str(total))

print(total)
