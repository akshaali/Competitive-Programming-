"""
Two players called  and  are playing a game with a starting number of stones. Player  always plays first, and the two players move in alternating turns. The game's rules are as follows:

In a single move, a player can remove either , , or  stones from the game board.
If a player is unable to make a move, that player loses the game.
Given the starting number of stones, find and print the name of the winner.  is named First and  is named Second. Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.

For example, if ,  can make the following moves:

 removes  stones leaving .  will then remove  stones and win.
 removes  stones leaving .  cannot move and loses.
 would make the second play and win the game.

Function Description

Complete the gameOfStones function in the editor below. It should return a string, either First or Second.

gameOfStones has the following parameter(s):

n: an integer that represents the starting number of stones
Input Format

The first line contains an integer , the number of test cases.
Each of the next  lines contains an integer , the number of stones in a test case.

Constraints

Output Format

On a new line for each test case, print First if the first player is the winner. Otherwise print Second.

Sample Input

8
1
2
3
4
5
6
7
10
Sample Output

Second
First
First
First
First
First
Second
First
Explanation

In the sample, we have  testcases.

If ,  can't make any moves and loses the game.

If ,  removes  stones and wins the game.

If ,  removes  stones in their first move, leaving  stone on the board and winning the game.

If ,  removes  stones in their first move, leaving  stone on the board and winning the game.

If ,  removes all  stones from the game board, winning the game.

If ,  removes  stones in their first move, leaving  stone on the board and winning the game.

If ,  can make any of the following three moves:

Remove  stones, leaving  stones on the board.  then removes  stones, winning the game.
Remove  stones, leaving  stones on the board.  then removes  stones, leaving  stone left on the board and winning the game.
Remove  stones, leaving  stones on the board.  then removes the  remaining stones and wins the game.
All possible moves result in  winning.

If ,  can remove either  or  stones to win the game.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfStones function below.
def gameOfStones(n):
    if n%7 == 0 or n%7 == 1:
        return("Second")
    else:
        return("First")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
