"""
There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.

For example, given three attendees' data as follows:

10101
11110
00010
These are all possible teams that can be formed:

Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]
In this case, the first team will know all 5 subjects. They are the only team that can be created knowing that many subjects.

Function Description

Complete the acmTeam function in the editor below. It should return an integer array with two elements: the maximum number of topics any team can know and the number of teams that can be formed that know that maximum number of topics.

acmTeam has the following parameter(s):

topic: a string of binary digits
Input Format

The first line contains two space-separated integers  and , where  represents the number of attendees and  represents the number of topics.

Each of the next  lines contains a binary string of length . If the th line's th character is , then the th person knows the th topic.

Constraints



Output Format

On the first line, print the maximum number of topics a 2-person team can know.
On the second line, print the number of ways to form a 2-person team that knows the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2
"""

Solution 1:
Long one perhaps :
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    max_q = 0
    max_t = 0
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            q = 0
            for k in range(len(topic[0])):
                print(topic[i][k],topic[j][k])
                if topic[i][k]=="1" or topic[j][k]=="1":
                    q +=1
            
            print(q)
            print("jxk")
            if q == max_q:
                max_t +=1 
            if q > max_q:
                max_q = q
                max_t = 1 
    return str(max_q), str(max_t)

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

Solution 2:

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the acmTeam function below.
def acmTeam(topics):
    comb = combinations(topics,2)
    m = 0
    count = 0
    for i in comb:
        n = str(bin(int(i[0],2) | int(i[1],2)))[2:].count('1')
        if n > m:            
            m = n
            count = 1
        elif n == m:
            count += 1
    return (m, count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()























