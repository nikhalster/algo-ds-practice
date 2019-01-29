#!/bin/python3

import math
import os
import random
import re
import sys

# def binarySearch(days, daily_rate, goal):
#     if daily_rate * days == goal:
#         return days
#     elif daily_rate * days > goal:
        

# Complete the minTime function below.
# def minTime(machines, goal):

    #Timed out solution
    # items_produced = 0 
    # for day in range(1, 100000):

    #     for machine_rate in machines:
    #         if day % machine_rate == 0:
    #             items_produced += 1

    #     if items_produced == goal:
    #         break
    # return day
# global result
# result = 0
# def binarySearch(days, daily_rate, goal):
#     global result
#     days = int(days)
#     rate_days = daily_rate * days
#     if rate_days == goal:
#         result = days
#     elif rate_days > goal:
#         binarySearch(days / 2, daily_rate, goal)
#     elif rate_days < goal:
#         binarySearch(days * 2, daily_rate, goal)
#
#
# # Complete the minTime function below.
# def minTime(machines, goal):
#
#     daily_rate = 0
#
#     for machine_rate in machines:
#         daily_rate += (1 / machine_rate)
#
#     days = 500
#
#     return binarySearch(days, daily_rate, goal)
#
# minTime([4,5,6], 12)
# print(result)


# global result
# result = 0
#
#
# def binarySearch(days, daily_rate, goal, left, right):
#     global result
#     mid = int(left + (right - left) / 2)
#
#     day = days[mid]
#     rate_days = daily_rate * day
#     if rate_days == goal:
#         result = day
#     elif rate_days > goal:
#         binarySearch(days, daily_rate, goal, left, mid - 1)
#     elif rate_days < goal:
#         binarySearch(days, daily_rate, goal, mid + 1, right)
#
#
# # Complete the minTime function below.
# def minTime(machines, goal):
#     daily_rate = 0
#
#     for machine_rate in machines:
#         daily_rate += (1 / machine_rate)
#
#     days = [day for day in range(0, 500)]
#     print(days)
#     binarySearch(days, daily_rate, goal, 0, len(days))
#     return result

def minTime(machines, goal):
    minday = math.ceil(goal / len(machines)) * min(machines)
    maxday = math.ceil(goal / len(machines) * max(machines))
    while minday < maxday:
        items_produced = 0
        day = (maxday + minday) // 2
        for m in machines:
            items_produced += int(day / m)
        if items_produced >= goal:
            maxday = day
        else:
            minday = day + 1
    return minday    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()

