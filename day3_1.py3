#!/usr/bin/env python

import sys
import math

puzzle_input=int(sys.argv[1])

def spiral_diag(n):
    return (2*n+1)**2 - 1 # OEIS A033996

def spiral_midpoints(n):
    return math.ceil((n**2+n+1)/4) # OEIS A039823

if puzzle_input==1:
    print("0 steps")
    exit()

diag_steps=0
mid_n=0

while True:
    if spiral_diag(diag_steps)>=puzzle_input:
        break
    else:
        diag_steps+=1

while True:
    if spiral_midpoints(mid_n)>=puzzle_input:
        curr_midpoint_diff=spiral_midpoints(mid_n)-puzzle_input
        last_midpoint_diff=puzzle_input-spiral_midpoints(mid_n-1)
        mid_steps=min(curr_midpoint_diff,last_midpoint_diff)
        break
    else:
        mid_n+=1

steps=diag_steps+mid_steps

print("Go "+str(mid_steps)+" steps along the edge and then "+
      str(diag_steps)+" steps to the center ("+str(steps)+" total)")
