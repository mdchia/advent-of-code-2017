#!/usr/bin/env python

import sys

filename = sys.argv[1]

memory = {}
max_val = 0

def process_instruction(s, register, max_val):
    command = s.split(" if ")[0]
    condition = s.split(" if ")[1]
    test_var = condition.split(" ")[0]
    change_var = command.split(" ")[0]
    if not(test_var in register):
        register[test_var]=0
    if not eval(str(register[test_var])+
            condition.split(" ")[1]+condition.split(" ")[2]):
        return max_val
    command = command.split(" ")
    if not(command[0] in register):
        register[change_var]=0
    if command[1] == "inc":
        register[change_var]+=int(command[2])
        if max_val < register[change_var]:
            print("New high: "+str(register[change_var]))
            return register[change_var]
        return max_val
    else:
        register[change_var]-=int(command[2])
        return max_val


with open(filename) as f:
    for line in f:
        max_val=process_instruction(line, memory, max_val)

print(memory)
print("Largest memory value after processing: "+str(max(memory.values())))
print("Largest memory value during processing: "+str(max_val))
