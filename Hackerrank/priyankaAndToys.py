"""
Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

For example, there are items with weights . This can be broken into two containers:  and . Each container will contain items weighing within  units of the minimum weight item.

Function Description

Complete the toys function in the editor below. It should return the minimum number of containers required to ship.

toys has the following parameter(s):

w: an array of integers that represent the weights of each order to ship
Input Format

The first line contains an integer , the number of orders to ship.
The next line contains  space-separated integers, , representing the orders in a weight array.

Constraints



Output Format

Return the integer value of the number of containers Priyanka must contract to ship all of the toys.

Sample Input

8
1 2 3 21 7 12 14 21
Sample Output

4
Explanation

The first container holds items weighing ,  and . (weights in range )
The second container holds the items weighing  units. ()
The third container holds the item weighing  units. ()
The fourth container holds the items weighing  and  units. ()

 containers are required.
 """
 
 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    l = sorted(w)
    coun = 0
    i = 0
    base = 0
    while (i != len(l)):
        coun +=1
        base = l[i]
        while (i != len(l) and l[i] <= base + 4):
            i += 1
        if i == len(l):
            break
    return coun

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()



"""
C++ solution :
        sort(w.begin(), w.end());
    int i=0, count=0, base;
    while(i!=w.size())
    {
        count++;
        base = w[i];
        while(i!=w.size() && w[i]<=base+4)
            i++;
        if (i==w.size())    break;
    }
    return count;
}
"""
