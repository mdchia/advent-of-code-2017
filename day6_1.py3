#!/usr/bin/env python

import sys

filename = sys.argv[1]

states = []
distributions = 0

with open(filename) as f:
    for line in f:
        line = line.split("\t")
        nums = [int(x) for x in line]
        break # only want first line

while True:
    save_curr = str(nums)
    print("Current state:"+save_curr)
    if save_curr in states:
        break
    else:
        states.append(save_curr)
        distributions+=1
    biggest_idx=nums.index(max(nums))
    amount_to_distribute = nums[biggest_idx]
    nums[biggest_idx] = 0 # remove values from cell
    curr_idx = biggest_idx+1
    while amount_to_distribute > 0:
        if curr_idx >= len(nums):
            curr_idx = 0 # wrap around
        else:
            nums[curr_idx]+=1
            amount_to_distribute-=1
            curr_idx+=1


print("Loop detected in "+str(distributions)+" distributions")
