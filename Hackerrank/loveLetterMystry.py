"""
James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
The letter a may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

For example, given the string , the following two operations are performed: cde → cdd → cdc.

Function Description

Complete the theLoveLetterMystery function in the editor below. It should return the integer representing the minimum number of operations needed to make the string a palindrome.

theLoveLetterMystery has the following parameter(s):

s: a string
Input Format

The first line contains an integer , the number of queries.
The next  lines will each contain a string .

Constraints


 | s | 
All strings are composed of lower case English letters, *ascii[a-z], with no spaces.

Output Format

A single line containing the minimum number of operations corresponding to each test case.

Sample Input

4
abc
abcba
abcd
cba
Sample Output

2
0
4
2
Explanation

For the first test case, abc → abb → aba.
For the second test case, abcba is already a palindromic string.
For the third test case, abcd → abcc → abcb → abca → abba.
For the fourth test case, cba → bba → aba.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    coun = 0
    n = len(s)
    for i in range(n//2):
        coun += abs(ord(s[i]) - ord(s[n-i-1]))
    return coun 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
