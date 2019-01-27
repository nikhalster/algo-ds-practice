#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    s1dict = {}
    s2dict = {}
    counter = 0
    for m in a:
        s1dict[m] = s1dict.get(m, 0) + 1
    for m in b:
        s2dict[m] = s2dict.get(m, 0) + 1

    for key, val in s1dict.items():
        if key in s2dict.keys():
            if s1dict[key] != s2dict[key]:
                counter += abs(s1dict[key] - s2dict[key])
        else:
            counter += s1dict[key]

    for key, val in s2dict.items():
        if key not in s1dict.keys():
            counter += s2dict[key]
        

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

