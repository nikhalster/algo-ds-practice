#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    # a,b,c = set(a), set(b), set(c)
    # O(n3) solution
    # for num2 in b:
    #     for num1 in a:
    #         for num3 in c:
    #             if num2 >= num3 and num1 <= num2:
    #                 count += 1

    a = (sorted(set(a)))
    b = (sorted(set(b)))
    c = (sorted(set(c)))
    
    i = 0
    j = 0    
    ans = 0
    
    for num2 in b:
        while i < len(a) and a[i] <= num2:
            i += 1
        
        while j < len(c) and c[j] <= num2:
            j += 1
        
        ans += i * j
    
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

