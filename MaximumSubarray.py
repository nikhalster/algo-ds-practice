#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def maximumSum(a, m, size):
    # sublist = []
    # modlist = [] 
      
    # first loop  
    # for i in range(len(a) + 1): 
          
    #     # second loop  
    #     for j in range(i + 1, len(a) + 1): 
              
    #         # slice the subarray  
    #         sub = a[i:j] 
    #         sublist.append(sub)
    # for subli in sublist:
    #     print(subli)

    #     modlist.append(sum(subli) % m)
    # return max(modlist)
    sums = []
    sum_value = 0
    for element in a:
        sum_value += element
        sums.append(sum_value)
    print(sums)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m, n)

        fptr.write(str(result) + '\n')

    fptr.close()

