"""
Our friends Alpha and Beta found a magical treasure of Asgard. It consists of  piles of gold coins. It is magical since if anyone tries to take a pile of  coins, all the other piles of exactly  coins (if they exist) disappear.

Alpha and Beta only have one turn each to choose a pile for themselves starting with Alpha. In one turn, a complete pile of gold coins can be chosen and since our friends are smart they will choose the pile with the maximum coins.

Find the number of coins Beta will get in his turn.

Function Description

Complete the alphaBeta function in the editor below. It should return an integer representing the number of coins Beta will get in his turn.

alphaBeta has the following parameter(s):

pile: an integer array

Input Format

First line of the input contains a single integer , number of piles.
Second line of the input contains  space seperated integers, number of gold coins in each pile.
Constraints

 (where )
Output Format

Single integer which is the number of coins Beta will receive in his first turn.
Sample Input 0

6
1 2 3 3 2 1
Sample Output 0

2
Explanation 0

Alpha will select a pile of  coins in his turn. So due to magic the other pile of  coins will disappear and Beta will be left with 4 piles:

1 2 2 1
Hence Beta will select a pile of  coins.

Sample Input 1

5
1 2 3 4 5
Sample Output 1

4
Explanation 1

Alpha will select a pile of 5 coins in his turn. There are no other piles of 5  coins so none disappear. Hence Beta will select a pile of 4  coins.
""""


def alphaBeta(pile):
    l = max(pile)
    #pile.pop(pile.index(l))
    if len(pile) == 0:
        return 0
    ans = list(filter(lambda a: a!=l,pile))
    if len(ans) == 0:
        return 0
    return max(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    pile = list(map(int, input().rstrip().split()))

    result = alphaBeta(pile)

    fptr.write(str(result) + '\n')

    fptr.close()
