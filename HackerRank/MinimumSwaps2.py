#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    counter = 0
    for i in range(0, len(a)-1):
        while a[i] != i+1:
            val = a[i]-1
            a[i], a[val] = a[val], a[i]
            counter += 1

        
#         if a[i] != i + 1:
#             counter += 1
#             for j in range(0, len(a)):
#                 if a[j] == i + 1:
#                     a[i], a[j] = a[j], a[i]
#                     break
        
        
        #2nd solution
        # ind = a.index(i + 1)
        # if ind + 1 != a[ind]:
        #     counter += 1
        #     a[ind], a[i] = a[i], a[ind]
            
        
        # if arr[i] != i + 1:
            #place it in correct position
            # counter += 1
            # for j in range(0, len(arr)):
            #     if arr[j] == i+1:
            #         arr[i], arr[j] = arr[j], arr[i] 
    return counter
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

