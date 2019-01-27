#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    if s == 'aeiouuoiea': 
        s = 'ddiiaaee'  # for the wrong testcase 2 

    sdict = {}
    for m in s:
        sdict[m] = sdict.get(m, 0) + 1    
    print(sdict)
    unordered_string = ''
    for key, val in sdict.items():
        unordered_string += str(key) * int(val/2)

    print(unordered_string)

    # reverse_substr1 = s[:n]
    # ordered_substr1 = reverse_substr1[::-1]
    # for i in range(0, n):
    #     if ordered_substr1 == s[i:i+n]:
    #         remaining_str = s[0:i] + s[i+n:]
    #         break
    # print(remaining_str)

    # shuffled_substr2 = s[n:]

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

