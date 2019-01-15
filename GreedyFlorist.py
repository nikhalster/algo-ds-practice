#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(n, k, c):
    c = sorted(c, reverse=True)
    increment = 2
    totalCost = 0

    for i in range(0, n):
        totalCost += ((i // k)+1) * c[i]
        #print(totalCost)
    # for price in c:

    #     if k > 0:
    #         totalCost += price
    #         k -= 1
    #     else:
    #         totalCost += price * increment

    return totalCost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(n, k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

