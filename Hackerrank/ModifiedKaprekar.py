"""
A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number  with  digits. We square  to arrive at a number that is either  digits long or  digits long. Split the string representation of the square into two parts,  and . The right hand part,  must be  digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get .

For example, if ,  then . We split that into two strings and convert them back to integers  and . We test , so this is not a modified Kaprekar number. If , still , and . This gives us , the original .

Note: r may have leading zeros.

Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!):

In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.

Given two positive integers  and  where  is lower than , write a program to print the modified Kaprekar numbers in the range between  and , inclusive.

Function Description

Complete the kaprekarNumbers function in the editor below. It should print the list of modified Kaprekar numbers in ascending order.

kaprekarNumbers has the following parameter(s):

p: an integer
q: an integer
Input Format

The first line contains the lower integer limit .
The second line contains the upper integer limit .

Note: Your range should be inclusive of the limits.

Constraints


Output Format

Output each modified Kaprekar number in the given range, space-separated on a single line. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.

Sample Input

1
100
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    m = 0
    for i in range(p, q+1):
       
        d = len(str(i))
        k = len(str(i**2))
        sq = str(i*i)
        r = int(sq[k-d:])
        #r = int(rs.lstrip("0"))
        try:
            l = int(sq[:k-d])
        except:
            l = 0
        
        #print(i)

        #print(l,r,i)
        if (i==1):
            m +=1 
            print(i, end=" ")
       
        elif (r+l==i):
            m +=1
            print(i, end=" ")
    if m == 0:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
