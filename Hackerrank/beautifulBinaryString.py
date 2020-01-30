"""
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alice's string is  she can change any one element and have a beautiful string.

Function Description

Complete the beautifulBinaryString function in the editor below. It should return an integer representing the minimum moves required.

beautifulBinaryString has the following parameter(s):

b: a string of binary digits
Input Format

The first line contains an integer , the length of binary string.
The second line contains a single binary string .

Constraints

.
Output Format

Print the minimum number of steps needed to make the string beautiful.

Sample Input 0

7
0101010
Sample Output 0

2  
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    n = len(b)
    coun = 0
    return b.count("010")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
