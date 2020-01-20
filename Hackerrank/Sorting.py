"""
his is a simple challenge to get things started. Given a sorted array () and a number (), can you print the index location of  in the array?

For example, if  and , you would print  for a zero-based index array.

If you are going to use the provided code for I/O, this next section is for you.

Function Description

Complete the introTutorial function in the editor below. It must return an integer representing the zero-based index of .

introTutorial has the following parameter(s):

arr: a sorted array of integers
V: an integer to search for
The next section describes the input format. You can often skip it, if you are using included methods or code stubs.

Input Format

The first line contains an integer, , a value to search for.
The next line contains an integer, , the size of . The last line contains  space-separated integers, each a value of  where .

Output Format
Output the index of  in the array.

The next section describes the constraints and ranges of the input. You should check this section to know the range of the input.

Constraints

It is guaranteed that  will occur in  exactly once.
This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge.

Sample Input 0

4
6
1 4 5 7 9 12
Sample Output 0

1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return(i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
