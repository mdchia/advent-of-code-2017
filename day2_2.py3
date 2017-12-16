#!/usr/bin/env python

import sys
import csv

filename = sys.argv[1]
total=0
done=False

with open(filename) as tsv:
    for row in csv.reader(tsv, dialect="excel-tab"):
        #row=row[0].split(" ") #if it's cut and pasted with spaces
        nums=[int(x) for x in row]

        for x in nums:
            for y in nums:
                if x<=y:
                    continue
                print("testing "+str(x)+"/"+str(y)+":"+str(x%y))
                if (x%y)==0:
                    result=x//y
                    done=True
                    break
            if done:
                done=False
                break
        print(nums)
        print(str(x)+"/"+str(y)+"="+str(result))
        total+=result

print("Sum of differences: "+str(total))
