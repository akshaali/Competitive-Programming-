"""
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
For example, the four players on the leaderboard have high scores of , , , and . Those players will have ranks , , , and , respectively. If Alice's scores are ,  and , her rankings after each game are ,  and .

Function Description

Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element  represents Alice's rank after the  game.

climbingLeaderboard has the following parameter(s):

scores: an array of integers that represent leaderboard scores
alice: an array of integers that represent Alice's scores
Input Format

The first line contains an integer , the number of players on the leaderboard.
The next line contains  space-separated integers , the leaderboard scores in decreasing order.
The next line contains an integer, , denoting the number games Alice plays.
The last line contains  space-separated integers , the game scores.

Constraints

 for 
 for 
The existing leaderboard, , is in descending order.
Alice's scores, , are in ascending order.
Subtask

For  of the maximum score:

Output Format

Print  integers. The  integer should indicate Alice's rank after playing the  game.

Sample Input 1

CopyDownload
Array: scores
100
100
50
40
40
20
10

 



Array: alice
5
25
50
120

 
7
100 100 50 40 40 20 10
4
5 25 50 120
Sample Output 1

6
4
2
1
"""


n = int(input())
#print(n)
scores = list(map(int, input().split()))
#print(score)
m = int(input())
alices = list(map(int, input().split()))
def climbingLeaderboard(scores, alices):
    unique_scores = list(reversed(sorted(set(scores))))

    i = len(alices)-1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alices[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1

    ans = ans[::-1]
    for i in ans:
        print(i)
            
climbingLeaderboard(scores, alices)
