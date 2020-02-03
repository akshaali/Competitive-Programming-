"""
Given two integers,  and , find the maximal value of  xor , written , where  and  satisfy the following condition:


For example, if  and , then



Our maximum value is .

Function Description

Complete the maximizingXor function in the editor below. It must return an integer representing the maximum value calculated.

maximizingXor has the following parameter(s):

l: an integer, the lower bound, inclusive
r: an integer, the upper bound, inclusive
Input Format

The first line contains the integer .
The second line contains the integer .

Constraints

3

Output Format

Return the maximal value of the xor operations for all permutations of the integers from  to , inclusive.

Sample Input 0

10
15
Sample Output 0

7
Explanation 0

The input tells us that  and . All the pairs which comply to above condition are the following:

Here two pairs (10, 13) and (11, 12) have maximum xor value 7, and this is the answer.

Sample Input 1

11
100
Sample Output 1

127
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    m = 0
    for i in range(l,r+1):
        for j in range(i, r+1):
            if m < i^j:
                m = i^j
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
