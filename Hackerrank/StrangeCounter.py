"""
Bob has a strange counter. At the first second, it displays the number . Each second, the number displayed by the counter decrements by  until it reaches .

The counter counts down in cycles. In next second, the timer resets to  and continues counting down. The diagram below shows the counter values for each time  in the first three cycles:

Find and print the value displayed by the counter at time .

Function Description

Complete the strangeCounter function in the editor below. It should return the integer value displayed by the counter at time .

strangeCounter has the following parameter(s):

t: an integer
Input Format

A single integer denoting the value of .

Constraints

Subtask

 for  of the maximum score.
Output Format

Print the value displayed by the strange counter at the given time .

Sample Input

4
Sample Output

6

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2

    return (rem-t+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
