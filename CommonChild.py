#https://medium.com/@carlosbf/common-child-solution-2e3d6dfb2004
#https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
#https://www.youtube.com/watch?v=NnD96abizww

import numpy as np

# def commonChild(s1, s2):
#     n = len(s1)
#     m = len(s2)
#     CCi = [0] * (m + 1)
#     CCj = [0] * (m + 1)
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 CCj[j] = CCi[j - 1] + 1
#             elif CCi[j] > CCj[j - 1]:
#                 CCj[j] = CCi[j]
#             else:
#                 CCj[j] = CCj[j - 1]
#         CCi = CCj
#         CCj = [0] * (m + 1)
#     return CCi[-1]

def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [x[:] for x in [[0] * (n+1)] * (m+1)]  #np.zeros((n+1,m+1))
    for i in range(1, n + 1):
         for j in range(1, m + 1):
             if s1[i-1] == s2[j-1]:
                 matrix[i][j] = matrix[i-1][j-1] + 1
             else:
                 matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    return matrix[n][m]

print(commonChild('SHINCHAN','NOHARAAA'))
