#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # for i in range(0, d):
    #     firstelement = a[0]
    #     a[0:leng-1] = a[1:leng]
    #     a[leng-1] = firstelement
    leng = len(a)
    
    b = a[d:leng]
    b[leng:] = a[:d]
    # b.append( for i in a[0:0+d])
    #### a[d:] + a[:d]    -->> best solution
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

