"""
You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price,  dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale will be sold at  dollars, but every subsequent game you buy will be sold at exactly  dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to  dollars, after which every game you buy will cost  dollars each.

For example, if ,  and , then the following are the costs of the first  games you buy, in order:

You have  dollars in your Mist wallet. How many games can you buy during the Halloween Sale?

Input Format

The first and only line of input contains four space-separated integers , ,  and .

Constraints

Output Format

Print a single line containing a single integer denoting the maximum number of games you can buy.

Sample Input 0

20 3 6 80
Sample Output 0

6
Explanation 0

We have ,  and , the same as in the problem statement. We also have  dollars. We can buy  games since they cost  dollars. However, we cannot buy a th game. Thus, the answer is .

Sample Input 1

20 3 6 85
Sample Output 1

7
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    
    coun = 0
    """
    while(s>0):
        if coun == 0:
            s = s-p
            coun +=1
        else:
            if p <= m:
                p = p-d
                s = s-p
                coun +=1 
            else:
                p = m 
                s = s-p
                coun +=1 
    """
    while s>=p:
        coun +=1 
        s = s-p
        p = max(p-d,m)
        
    return coun


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
