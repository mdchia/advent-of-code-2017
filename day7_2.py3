#!/usr/bin/env python

import sys
from collections import Counter

filename = sys.argv[1]

with_children =[]
main_tree = {}

class TreeNode(object):
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def add_child(self, child_name):
        self.children.append(child_name)

    def set_parent(self, parent):
        self.parent = parent

def find_root(tree):
    node = next (iter (tree.values()))
    while node.parent != None:
        print("Current node is "+node.name+" a child of "+node.parent)
        node = tree[node.parent]
    return node.name

def print_tree(nodename, tree, n):
    print(("   "*n)+nodename+", weight: "+str(tree[nodename].weight))
    for child in tree[nodename].children:
        print_tree(child, tree, n+1)

def get_weight(nodename, tree):
    node = tree[nodename]
    weight = node.weight
    if node.children:
        for child in node.children:
            weight+=get_weight(child, tree)
    return weight

def find_unbalanced(rootname, tree, n):
    # assumes >2 children with exactly one imbalanced
    curr_node = tree[rootname]
    level = {}
    if curr_node.children == []:
        return False
    for child in curr_node.children:
        weight=get_weight(child, tree)
        level[child]=weight
    if len(set(level.values())) == 1:
        print("Balanced!")
        return True
    else:
        wc=Counter(level.values())
        abnormal=wc.most_common()[-1][0] # get the value which occurs the least
        imbalanced=list(level.keys())[list(level.values()).index(abnormal)]
        normal_weight=wc.most_common()[0][0]
        broken_node = tree[imbalanced]
        subweight=abnormal-broken_node.weight
        fixed_weight=normal_weight-subweight

        print("Unbalanced: normal is "+str(normal_weight)+
              ", unbalanced is "+str(abnormal)+" @ level "+str(n))
        if find_unbalanced(imbalanced, tree, n+1):
            print("Fix node "+imbalanced+" at level "+str(n)+
                  " by changing weight from "+
                  str(broken_node.weight)+" to "+str(fixed_weight)+
                  " to bring all children at level to weight "+
                  str(normal_weight))

        return False


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
        weight = main_tree[child].weight
        main_tree[parent].add_child(child)
        main_tree[child].parent = parent

print("Finding root ...")
rootname = find_root(main_tree)
print("Root program is "+rootname)
print_tree(rootname, main_tree, 0)

print("Finding unbalanced node ...")
find_unbalanced(rootname, main_tree, 1)
