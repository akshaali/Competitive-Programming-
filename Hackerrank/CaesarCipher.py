"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
For example, the given cleartext  and the alphabet is rotated by . The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below. It should return the encrypted string.

caesarCipher has the following parameter(s):

s: a string in cleartext
k: an integer, the alphabet rotation factor
Input Format

The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.

Constraints



 is a valid ASCII string without any spaces.

Output Format

For each test case, print the encoded string.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    sa = ""
    k = k%26
    for i in s:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
            if i.islower():
                if (ord(i)+k>=97 and ord(i)+k<=122):
                    sa += (chr(ord(i)+k))
                else:
                     sa += chr(-122+97+ord(i)+k-1)
            else:
                if (ord(i)+k) >= 65 and ord(i)+k <= 90:
                    sa += chr(ord(i)+k)
                else:
                    sa += chr(-90+65+ord(i)+k-1)
        else: 
            sa +=i
    return sa        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
