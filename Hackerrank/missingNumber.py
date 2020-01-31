"""
Numeros the Artist had two lists that were permutations of one another. He was very proud. Unfortunately, while transporting them from one exhibition to another, some numbers were lost out of the first list. Can you find the missing numbers?

As an example, the array with some numbers missing, . The original array of numbers . The numbers missing are .

Notes

If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
The difference between maximum and minimum number in the second list is less than or equal to .
Function Description

Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):

arr: the array with missing numbers
brr: the original array of numbers
Input Format

There will be four lines of input:

 - the size of the first list, 
The next line contains  space-separated integers 
 - the size of the second list, 
The next line contains  space-separated integers 

Constraints

Output Format

Output the missing numbers in ascending order.

Sample Input

10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
Sample Output

204 205 206
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    """
    ar = {}
    br = {}
    for i in set(arr):
        ar[i] = arr.count(i)
    for j in set(brr):
        br[j] = brr.count(j)
    print(ar, br)
    
    aMin = min(arr)
    bMin = min(brr)
    tMin = min(aMin, bMin)
    
    aMax = max(arr)
    bMax = max(brr)
    tMax = max(aMax, bMax)
    """
    l = [0]*10001
    for i in range(len(arr)):
        l[arr[i]] -=1
    for i in range(len(brr)):
        l[brr[i]] +=1
    q = []
    for i in range(10001):
        if l[i] > 0:
            q.append(i)
    return q


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
