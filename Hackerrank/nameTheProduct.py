"""
You are contesting to name a new product in your company given the following conditions:

You are given an array of  different names, , where  denotes the  name and all the names are of length . The distance between any two names is the number of positions in which the characters in these names differ. For example, "bubby" and "bunny" differ in two positions.

You have to choose a name such that the sum of differences of all names in  with the chosen name is maximal. In order to win the contest, give the new product this chosen name.

Note: If there are many such names chose the lexicographically largest one.

Take for example, names = ["bubby", "bunny", "berry"], with length . Then, the name that you should choose is "zzzzz" as this name has no common character with any name in the names list and is also lexicographically the largest.

Function Description

Complete the productName function in the editor below. It should return the lexigraphically largest string of length  whose sum of differences with all the names is maximal.

productName has the following parameter(s):

names: array of  names

Input Format

The first line contains an integer, , denoting the number of elements in .
Each line  of the  subsequent lines (where ) contains a string describing .
Constraints

All characters in the names are lowercase English alphabets.
Each name is of length .
Output Format

The output should contain the lexigraphically largest string of length  whose sum of differences with all the names is maximal.
Sample Input 0

3
bubby
bunny
berry
Sample Output 0

zzzzz
Explanation 0

Difference between , bubby, and zzzzz is .
Difference between , bunny, and zzzzz is .
Difference between , berry, and zzzzz is .
So, total difference is 15, which is maximal.

Sample Input 1

3
ready
stedy
zebra
Sample Output 1

yzzzz
Explanation 1

Difference between , ready, and yzzzz is .
Difference between , stedy, and yzzzz is .
Difference between , zebra, and yzzzz is .
So, total differce is 15, which is maximal.
"""

def productName(names):
    ans = [[0 for i in range(26)] for j in range(5)]
    #i = 0
    #while i <5:
    #    l = []
    for n in range(len(names)):
        for k in range(5):
             ans[k][ord(names[n][k])-97] += 1
    ans = [i[::-1] for i in ans]
    result = []
    for i in range(5):
        result.append(chr(122 - ans[i].index((min(ans[i])))))
    print(ans,result)
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    names = []

    for _ in range(n):
        names_item = input()
        names.append(names_item)

    result = productName(names)

    fptr.write(result + '\n')

    fptr.close()
