"""
Consider an array of numeric strings where each string is a positive number with anywhere from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.

Function Description

Complete the bigSorting function in the editor below. It should return the sorted string array.

bigSorting has the following parameter(s):

unsorted: an unsorted array of integers as strings
Input Format

The first line contains an integer, , denoting the number of strings in .
Each of the  subsequent lines contains an integer string .

Constraints

Each string is guaranteed to represent a positive integer without leading zeros.
The total number of digits across all strings in  is between  and  (inclusive).
Output Format

Print each element of the sorted array on a new line.

Sample Input 0

6
31415926535897932384626433832795
1
3
10
3
5
Sample Output 0

1
3
3
5
10
31415926535897932384626433832795
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):

    unsorted.sort(key=int)
    return unsorted
    """
    for s in unsorted:
        return(s)
    
    for i in range(len(unsorted)):
        for j in range(i+1, len(unsorted)):
            if len(unsorted[i])> len(unsorted[j]):
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
    return unsorted
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    #print(result)
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
