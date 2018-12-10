#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    sumPrice = 0
    counter = 0 
    for i in range(0, len(sortedPrices)):
        if sumPrice + sortedPrices[i] < k: 
            sumPrice += sortedPrices[i]
            counter += 1
    return counter        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
