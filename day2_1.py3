#!/usr/bin/env python

import sys
import csv

filename = sys.argv[1]
total=0

with open(filename) as tsv:
    for row in csv.reader(tsv, dialect="excel-tab"):
        #nums=row[0].split(" ")

        nums=[int(x) for x in row]
        biggest=max(nums)
        smallest=min(nums)
        diff = biggest-smallest
        print(nums)
        print(str(biggest)+", "+str(smallest)+":"+str(diff))
        total+=diff

print("Sum of differences: "+str(total))
