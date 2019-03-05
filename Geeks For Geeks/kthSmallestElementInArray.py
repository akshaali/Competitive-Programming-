"""
Given an array arr and a number K where K is smaller than size of array, the task is to find the K’th smallest element in the given array. It is given that all array elements are distinct.

Expected Time Complexity: O(n)

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the desired output in a new line.

Constraints:
1 <= T <= 106
1 <= N <= 100
1 <= arr[i] <= 103
1 <= K <= N

Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4

Output:
7
15
"""
#code
t = int(input())
for _ in range(t):
    o = int(input())
    l = [int(x) for x in input().split()]
    #print(l)
    s = input()
    l = sorted(l)
    print(l[int(s)-1])
    
