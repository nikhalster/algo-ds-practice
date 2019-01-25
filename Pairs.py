#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr = sorted(arr)
    counter = 0
    n = len(arr)
    i=0
    j=1
    while( j < n ):
        difference = arr[j] - arr[i]
        if difference == k:
            counter += 1
            j += 1
        elif difference < k:
            j += 1
        elif difference > k:
            i += 1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

