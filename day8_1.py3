#!/usr/bin/env python

import sys

filename = sys.argv[1]

memory = {}

def process_instruction(s, register):
    command = s.split(" if ")[0]
    condition = s.split(" if ")[1]
    test_var = condition.split(" ")[0]
    change_var = command.split(" ")[0]
    if not(test_var in register):
        register[test_var]=0
    if not eval(str(register[test_var])+
            condition.split(" ")[1]+condition.split(" ")[2]):
        return False
    command = command.split(" ")
    if not(command[0] in register):
        register[command[0]]=0
    if command[1] == "inc":
        register[command[0]]+=int(command[2])
    else:
        register[command[0]]-=int(command[2])


with open(filename) as f:
    for line in f:
        process_instruction(line, memory)

print(memory)
print(max(memory.values()))
