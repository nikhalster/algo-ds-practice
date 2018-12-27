#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(n, queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swapped = False
    
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    for i in range(lastIndex):
        for j in range(lastIndex):
            if queue[j] > queue[j+1]:
                queue[j], queue[j+1] = queue[j+1], queue[j]
                swaps += 1
                swapped = True
        
        if swapped:
            swapped = False
        else:
            break
    return swaps

    # bribeCounter = 0
    # checkedList = []
    # i = n
    # while i >0:
    #     # print(i)
    #     if i in checkedList:
    #         i = i - 1
    #         continue
    #     if q[i - 1] == i:
    #         i = i -1
    #     elif q[i - 2] == i:
    #         bribeCounter += 1
    #         i = i - 1
    #         checkedList.append(q[i-1])
    #     elif q[i - 3] == i:
    #         bribeCounter += 2
    #         i = i - 1
    #         checkedList.append(q[i-2])
    #         checkedList.append(q[i-1])
    #     else:
    #         return "Too chaotic"
    #     print(bribeCounter)
    # return bribeCounter



            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(n, q))

