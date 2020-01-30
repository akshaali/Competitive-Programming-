"""
You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string , remove an  at positions  and  to make  in  deletions.

Function Description

Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

s: a string
Input Format

The first line contains an integer , the number of queries.
The next  lines each contain a string .

Constraints

Each string  will consist only of characters  and 
Output Format

For each query, print the minimum number of deletions required on a new line.

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output

3
4
0
0
4
Explanation

The characters marked red are the ones that can be deleted so that the string doesn't have matching consecutive characters.

image

Python 3


8910111213141516181920212223242567345262717
def alternatingCharacters(s):
    p = 0
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
          p +=1
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


Line: 11 Col: 28
Submit CodeRun Code
Upload Code as File
Test against custom input
Problem Solving
You have earned 20.00 points!
You are now 540.98 points away from the 6th star for your problem solving badge.
60%1659.02/2200
Congratulations
You solved this challenge. Would you like to challenge your friends?

Next Challenge
Test case 0
Test case 1
Test case 2
Test case 3
Test case 4
Test case 5
Test case 6
Test case 7
Test case 8
Test case 9
Test case 10
Test case 11
Test case 12
Test case 13
Test case 14
Compiler Message
Success
Input (stdin)
Download
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Expected Output
Download
3
4
0
0
4

"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.

def alternatingCharacters(s):
    p = 0
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
          p +=1
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


