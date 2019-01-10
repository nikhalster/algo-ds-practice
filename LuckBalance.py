#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luckTotal = 0
    contests = sorted(contests, reverse=True)
    for l, t in contests:
        if t == 0:       #Not important
            luckTotal += l
        else:    #important
            if k <= 0:    # Not allowed to lose contest
                luckTotal -= l
            else:
                k = k - 1
                luckTotal += l
    return luckTotal                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

