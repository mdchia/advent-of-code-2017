#!/usr/bin/env python

import sys
import csv

filename = sys.argv[1]

with_children =[]
main_tree = {}

class TreeNode(object):
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

def find_root(tree):
    node = next (iter (tree.values()))
    while node.parent != None:
        print("Current node is "+node.name+" a child of "+node.parent)
        node = tree[node.parent]
    return node.name

with open(filename) as f:
    for line in f:
        line = line.rstrip("\n")
        if line.find("->")!=-1:
            with_children.append(line)
        name = line.split(" (")[0]
        weight = int(line[line.find("(")+1:line.find(")")])
        curr_obj = TreeNode(name=name, weight=weight)
        print("Adding new program: "+name)
        main_tree[name]=curr_obj

while with_children!=[]:
    curr_line = with_children.pop()
    parent = curr_line.split(" (")[0]

    children = curr_line.split(" -> ")[1]
    children = children.split(", ")

    print("Adding chidren of program "+parent+": "+", ".join(children))
    for child in children:
        main_tree[parent].add_child(child)
        main_tree[child].parent = parent

print("Finding root ...")
rootname = find_root(main_tree)
print("Root program is "+rootname)
