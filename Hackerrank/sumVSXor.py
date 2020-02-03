"""
Given an integer , find each  such that:

where  denotes the bitwise XOR operator. Print the number of 's satisfying the criteria.

For example, if , there are four values:

.
Function Description

Complete the sumXor function in the editor below. It should return the number of values determined, as an integer.

sumXor has the following parameter(s):
- n: an integer

Input Format

A single integer, .

Constraints

Subtasks

 for  of the maximum score.
Output Format

Print the total number of integers  satisfying the criteria.

Sample Input 0

5
Sample Output 0

2
Explanation 0

For , the  values  and  satisfy the conditions:

Sample Input 1

10
Sample Output 1

4
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    if n == 0:
        return 1
    l = bin(n)[2:].count("0")
    return 2**l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
