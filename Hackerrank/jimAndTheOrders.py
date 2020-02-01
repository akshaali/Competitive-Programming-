"""
Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them. Determine the order the customers receive their orders. Start by numbering each of the customers from  to , front of the line to the back. You will then be given an order number and a preparation time for each customer.

The time of delivery is calculated as the sum of the order number and the preparation time. If two orders are delivered at the same time, assume they are delivered in ascending customer number order.

For example, there are  customers in line. They each receive an order number  and a preparation time .:

Customer	1	2	3	4	5
Order #		8	5	6	2	4
Prep time	3	6	2	3	3
Calculate:
Serve time	11	11	8	5	7
We see that the orders are delivered to customers in the following order:

Order by:
Serve time	5	7	8	11	11
Customer	4	5	3	1	2
Function Description

Complete the jimOrders function in the editor below. It should return an array of integers that represent the order that customers' orders are delivered.

jimOrders has the following parameter(s):

orders: a 2D integer array where each  is in the form .
Input Format

The first line contains an integer , the number of customers.
Each of the next  lines contains two space-separated integers, an order number and prep time for .

Constraints

Output Format

Print a single line of  space-separated customer numbers (recall that customers are numbered from  to ) that describes the sequence in which the customers receive their burgers. If two or more customers receive their burgers at the same time, print their numbers in ascending order.

Sample Input 0

3
1 3
2 3
3 3
Sample Output 0

1 2 3
Explanation 0

Jim has the following orders:

. This order is delivered at time .
. This order is delivered at time .
. This order is delivered at time .
The orders were delivered in the same order as the customers stood in line. The index in  is the customer number and is what is printed. In this case, the customer numbers match the order numbers.

Sample Input 1

5
8 1
4 2
5 6
3 1
4 3
Sample Output 1

4 2 5 1 3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    for i in range(len(orders)):
        orders[i].append(orders[i][0] + orders[i][1])
        orders[i].append(i+1)
    print(orders)
    orders = sorted(orders, key=lambda x: x[2])
    print(orders)
    l = []
    for i in range(len(orders)):
        l.append(orders[i][3])
    return(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
