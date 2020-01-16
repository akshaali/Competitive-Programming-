"""
Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.

For example, if his array is , we see that he can delete the  elements  and  leaving . He could also delete both twos and either the  or the , but that would take  deletions. The minimum number of deletions is .

Function Description

Complete the equalizeArray function in the editor below. It must return an integer that denotes the minimum number of deletions required.

equalizeArray has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer , the number of elements in .
The next line contains  space-separated integers .

Constraints

Output Format

Print a single integer that denotes the minimum number of elements Karl must delete for all elements in the array to be equal.

Sample Input

5
3 3 2 1 3
Sample Output

2   
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    l = list(set(arr))
    dic = {}
    for i in range(len(l)):
        dic[l[i]] = arr.count(l[i])
    max = 0
    for i,value in dic.items():
        if value > max :
            max = value 
    return len(arr)- max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
