"""
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

For example, given the string , the ordinal values of the charcters are .  and the ordinals are . The absolute differences of the adjacent elements for both strings are , so the answer is Funny.

Function Description

Complete the funnyString function in the editor below. For each test case, it should return a string, either Funny or Not Funny.

funnyString has the following parameter(s):

s: a string to test
Input Format

The first line contains an integer , the number of queries.
The next  lines each contain a string, .

Constraints

Output Format

For each string  print whether it is Funny or Not Funny on a new line.

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    n = len(s)
    for i in range(n-1):
        print(ord(s[i]), ord(s[i+1]), ord(s[n-i-1]), ord(s[n-2-i]))
        print(s[i], s[i+1], s[n-i-1], s[n-i-2])
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(s[n-i-1]) - ord(s[n-i-2])):
            return("Not Funny")



    return("Funny")
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
