#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    result = n
    for i, letter in enumerate(s):
        middle_letter = None
        for j in range(i+1, n):
            if letter == s[j]:
                if middle_letter is None:
                    result += 1
                elif j - middle_letter == middle_letter - i:
                    result += 1
                    break
            else:
                if middle_letter is None:
                    middle_letter = j
                else:
                    break
    return result


          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

