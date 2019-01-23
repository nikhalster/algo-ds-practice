#!/bin/python3
# http://openbookproject.net/thinkcs/python/english3e/trees.html
# 
import os
import sys

tree = []

class Node:

    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return "Node:- {} Right - {} Left {}".format(self.value, self.right, self.left)

def inorder(roots):
    # if type(roots) != Node or type(roots)!= None:
    #     for root in roots:
    #         if root:
    #             inorder(root.left)
    #             print(root.value)
    #             inorder(root.right)
    # else:
    if roots:
        inorder(roots.left)
        print(roots.value)
        inorder(roots.right)


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

    # inorder(initial_root)
        
    
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

