#!/usr/bin/env python

import sys
from collections import Counter

filename = sys.argv[1]
valid_passphrases = 0

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def is_passphrase_valid(pp):
    words=pp.split(" ")
    counts=Counter(words)
    for count in counts.values():
        if count > 1:
            return False
    for word1 in words:
        for word2 in words:
            if word1==word2:
                continue
            if is_anagram(word1, word2):
                return False
    return True

with open(filename) as f:
    passphrases = [line.rstrip('\n') for line in f]
    for passphrase in passphrases:
        if is_passphrase_valid(passphrase):
            valid_passphrases+=1

print(str(valid_passphrases)+" valid passphrases")
