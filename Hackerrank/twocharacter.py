"""
In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.

Given a string , convert it to the longest possible string  made up only of alternating characters. Print the length of string  on a new line. If no string  can be formed, print  instead.

Function Description

Complete the alternate function in the editor below. It should return an integer that denotes the longest string that can be formed, or  if it cannot be done.

alternate has the following parameter(s):

s: a string
Input Format

The first line contains a single integer denoting the length of .
The second line contains string .

Constraints

Output Format

Print a single integer denoting the maximum length of  for the given ; if it is not possible to form string , print  instead.

Sample Input

10
beabeefeab
Sample Output

5
Explanation

The characters present in  are a, b, e, and f. This means that  must consist of two of those characters and we must delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b), and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are consecutive e's present. Removing them would leave consecutive b's, so this fails to produce a valid string .

Other cases are solved similarly.

babab is the longest string we can create.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    def validate(cpy):
        for i in range(len(cpy)-1):
            if cpy[i] == cpy[i+1]:
                return False
        return True

    st = list(set(s))
    max_len = 0
    for x in range(len(st)):
        for y in range(x+1, len(st)):
            cpy = [c for c in s if c==st[x] or c==st[y]]
            if validate(cpy):
                max_len = max(max_len, len(cpy))
    return(max_len)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
