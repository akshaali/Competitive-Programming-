"""
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is , you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Function Description

Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.

pickingNumbers has the following parameter(s):

a: an array of integers
Input Format

The first line contains a single integer , the size of the array .
The second line contains  space-separated integers .

Constraints

The answer will be .
Output Format

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is .

Sample Input 0

6
4 6 5 3 3 1
Sample Output 0

3
Explanation 0

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

Sample Input 1

6
1 2 2 3 1 2
Sample Output 1

5

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    if a == None:
        return 0

    ai = list(set(a))
    dic = {}
    for i in ai:
        dic1 = {i:a.count(i)}
        dic.update(dic1)
    l = []
    f = 0
    print(dic)
    key1 = ai[0]
    value1 = dic[ai[0]]
    dic1 = dic.copy()
    del dic[ai[0]]
    print(dic)
    if not bool(dic):
        return value1
    for key, value in dic.items():
        if abs(key1-key) <=1:
            f = 1
            l.append(value1+value)
        key1 = key
        value1 = value 

    print(dic1)
    key_max = max(dic1.keys(), key=(lambda k: dic1[k]))
    if f:
        return max(max(l), dic1[key_max])
    else:
        key_max = max(dic1.keys(), key=(lambda k: dic1[k]))
        return key_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
