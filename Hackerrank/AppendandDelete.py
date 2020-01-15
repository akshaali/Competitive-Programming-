"""
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes. Otherwise, print No.

For example, strings  and . Our number of moves, . To convert  to , we first delete all of the characters in  moves. Next we add each of the characters of  in order. On the  move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than  moves, we would not have succeeded in creating the new string.

Function Description

Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

s: the initial string
t: the desired string
k: an integer that represents the number of operations
Input Format

The first line contains a string , the initial string.
The second line contains a string , the desired final string.
The third line contains an integer , the number of operations.

Constraints

 and  consist of lowercase English alphabetic letters, .
Output Format

Print Yes if you can obtain string  by performing exactly  operations on . Otherwise, print No.

Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes
Explanation 0

We perform  delete operations to reduce string  to hacker. Next, we perform  append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert  to  by performing exactly  operations, we print Yes.

Sample Input 1

aba
aba
7
Sample Output 1

Yes

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    commonLength = 0
    for i in range(min(len(t), len(s))):
        if s[i] == t[i]:
            commonLength +=1 
        else:
            break
    if len(s) + len(t) - 2*commonLength > k:
        return("No")
    elif (len(s) + len(t) - 2*commonLength)%2 == k%2:
        return("Yes")
    elif len(s) + len(t)-k < 0 :
        return("Yes")
    else:
        return("No")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
