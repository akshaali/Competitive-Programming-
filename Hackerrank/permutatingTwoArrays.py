"""
Consider two -element arrays of integers,  and . You want to permute them into some  and  such that the relation  holds for all  where . For example, if , , and , a valid  satisfying our relation would be  and ,  and .

You are given  queries consisting of , , and . For each query, print YES on a new line if some permutation ,  satisfying the relation above exists. Otherwise, print NO.

Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

k: an integer
A: an array of integers
B: an array of integers
Input Format

The first line contains an integer , the number of queries.

The next  sets of  lines are as follows:

The first line contains two space-separated integers  and , the size of both arrays  and , and the relation variable.
The second line contains  space-separated integers .
The third line contains  space-separated integers .
Constraints

Output Format

For each query, print YES on a new line if valid permutations exist. Otherwise, print NO.

Sample Input

2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4
Sample Output

YES
NO
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B)[::-1]
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
