#!/bin/python3
# http://openbookproject.net/thinkcs/python/english3e/trees.html
# 

import os
import sys
sys.setrecursionlimit(15000)

tree = []

class Node:

    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return "Node:- {} Right - {} Left {}".format(self.value, self.right, self.left)

def swap(root, l, q):
    if l % q == 0:
        root.left, root.right = root.right, root.left
    if root.left:
        swap(root.left, l + 1, q)
    if root.right:
        swap(root.right, l + 1, q)


def inorder(roots, inter_result):
    # if type(roots) != Node or type(roots)!= None:
    #     for root in roots:
    #         if root:
    #             inorder(root.left)
    #             print(root.value)
    #             inorder(root.right)
    # else:
    if roots:
        inorder(roots.left, inter_result)
        inter_result.append(roots.value)
        inorder(roots.right, inter_result)


# def inorder_traversal(root):



#
# Complete the swapNodes function below.
#
# def insert(root, indexes):
    
#     for left, right in indexes:
#         tree.append(root)
#         if left == None or right == None:
#             break

#         if left != -1:
#             tree[-1].left = left
#         if right != -1:
#             tree[-1].right = right
#         insert(Node(left), indexes[1:])
#         insert(Node(right), indexes[1:])

def swapNodes(indexes, queries):
    # insert(Node(1), indexes)
    initial_root = Node(1)
    tree = [initial_root]
    for i in range(0, len(indexes)):
        # root = rootList.po
        root = tree.pop(0)
        left = indexes[i][0]
        right = indexes[i][1]
        if left != -1:
            root.left = Node(left)
            tree.append(root.left)

        if right != -1:
            root.right = Node(right)
            tree.append(root.right)
    result = []
    for query in queries:
        inter_result = []
        swap(initial_root, 1, query)
        inorder(initial_root, inter_result)
        result.append(inter_result)
    return result
    
    # inorder(tree)#
    # print(tree)
        
           

    # for i, j in range(0, indexes)


        # print(right)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


