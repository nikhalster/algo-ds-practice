#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s1dict = {}
    s2dict = {}
    for c in s:
        s1dict[c] = s1dict.get(c, 0) + 1

    list_of_values = list((s1dict.values()))
    if len(list_of_values) == 1:
        return "YES"
    if len(set(list_of_values)) > 2:
        return "NO"
    elif abs(list_of_values[0] - list_of_values[1]) > 1:
        return "NO"

    for val in list_of_values:
        s2dict[val] = s2dict.get(val, 0) + 1
    list2 = list(s2dict.values())
    if len(list2) > 1:
        if list2[0] == 1 or list2[1] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "YES"

    # elif len(list_of_values) == 2:
    #     if abs(list_of_values[0] - list_of_values[1]) == 1:
    #         return "YES"
    # else:
    #     return "YES"
    # for val in s1dict.values():
    #     print(val)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

