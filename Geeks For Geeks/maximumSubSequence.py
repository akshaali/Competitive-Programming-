"""
Given an array A of N positive integers. Find the sum of maximum sum increasing subsequence of the given array.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N(the size of array). The second line of each test case contains array elements.

Output:
For each test case print the required answer in new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 ≤ Ai ≤ 106

Example:
Input:
2
7
1 101 2 3 100 4 5
4
10 5 4 3

Output:
106
10

Explanation:
Testcase 1: All the increasing subsequences are : (1,101); (1,2,3,100); (1,2,3,4,5). Out of these (1, 2, 3, 100) has maximum sum,i.e., 106.

"""


Solution 1:
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = arr[0]
    dp = arr.copy()
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i], dp[j]+arr[i])
            if ans<dp[i]:
                ans = dp[i]
    print(ans)
            
Complexity = O(n^2)

Solution 2:




        
        
        
