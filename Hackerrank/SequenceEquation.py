"""
Function Description

Complete the permutationEquation function in the editor below. It should return an array of integers that represent the values of .

permutationEquation has the following parameter(s):

p: an array of integers
Input Format

The first line contains an integer , the number of elements in the sequence.
The second line contains  space-separated integers  where .

Constraints

, where .
Each element in the sequence is distinct.
Output Format

For each  from  to , print an integer denoting any valid  satisfying the equation  on a new line.

Sample Input 0

3
2 3 1
Sample Output 0

2
3
1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l = []
    for i in range(1,len(p)+1):
        q = p.index((p.index(i))+1) +1
        l.append(q)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
