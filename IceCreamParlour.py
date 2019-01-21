# https://leetcode.com/articles/two-sum/
# https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf


#!/bin/python3

import math
import os
import random
import re
import sys

    

# Complete the whatFlavors function below.
def whatFlavors(cost, money, n):
    # cost_dict = {}
    # for index, c in enumerate(cost):
    #     cost_dict[index] = c
    # # print(cost_dict)

    # for key, val in cost_dict.items():
    #     if (money - val) in cost_dict.values():
    #         # print(cost_dict.values())
    #         print(key+1, cost.index(money-val)+1)
    #         # print(key + 1, cost_dict[money-val] + 1)
    #         break

    cost_dict = {}
    for pos, c in enumerate(cost):
        if c in cost_dict:
            print(cost_dict[c], pos + 1)
            break
        else:
            cost_dict[money-c] = pos + 1

   
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money, n)

