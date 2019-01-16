#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    min_val = 10**16
    arr = sorted((arr))
    for i in range(0, len(arr)-k+1):
        # subarr = arr[i:i+k]
        # if subarr[-1] - subarr[0] < min_val:
        #     min_val = subarr[-1] - subarr[0]
        if arr[i+k-1] - arr[i] < min_val:
            min_val = arr[i+k-1] - arr[i]
            
                
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

