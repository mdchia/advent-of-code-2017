#!/usr/bin/env python

import sys
from collections import Counter

filename = sys.argv[1]
total_jumps = 0
curr_i = 0

with open(filename) as f:
    jumps = [int(line) for line in f]

print("Maze is "+str(len(jumps))+" jumps large")

while True:
    if not (0 <= curr_i < len(jumps)):
        break
    jumps[curr_i]+=1 # increment where we are
    print("Jumping "+str(jumps[curr_i]-1)+" from position "+str(curr_i)+" to "+
          str(curr_i+(jumps[curr_i]-1)))
    curr_i = curr_i+(jumps[curr_i]-1)
    total_jumps+=1

print("Escaped in "+str(total_jumps)+" jumps")
