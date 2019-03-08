"""
Given a Binary Search Tree and 2 nodes value n1 and n2, your task is to find the lowest common ancestor(LCA) of the two nodes .

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input.
The first line contains N, the number of nodes of the BST.
The second line contains the values of the nodes, each separated by a space.
The third line contains the two values n1 and n2 separated by a space.

Output Format:
For each testcase, in a new line, print the LCA of n1 and n2.

Your Task:
This is a function problem. You don't have to take any input. You are required to complete the function LCA that takes node, n1, n2 as parameters and returns the node that is LCA of n1 and n2.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Node value <= 1000

Example:
Input
1
6
5 4 6 3 7 8
7 8

Output 
7

Explanation 
The BST in above test case will look like

    5
   /  \ 
  4  6
 /      \
3        7
            \ 
             8
here the LCA of 7 and 8 is 7 .
"""

{
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        a,b = list(map(int, input().strip().split()))
        res = LCA(root, a, b)
        print(res.data)
# Contributed by: Harshit Sidhwa
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# function should return the required lca node
def LCA(root, a, b):
    if root is None:
        return None
    if a < root.data and b < root.data:
        return LCA(root.left,a,b)
    if a > root.data and b > root.data:
        return LCA(root.right,a,b)
    return root
