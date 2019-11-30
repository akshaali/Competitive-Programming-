"""
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

"""
Solution 1:
T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(*arr)
    
    
 complexity = O(nLog(n))
    
 Solution 2:
 
 T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    count0, count1, count2 = 0,0,0
    for i in range(n):
        if arr[i] == 0:
            count0 +=1
        elif arr[i] == 1:
            count1 +=1
        else:
            count2 +=1
            
    arr[0:count0] = [0]*count0
    arr[count0:count1+count0] = [1]*count1
    arr[count1+count0:] = [2]*count2
    print(*arr)
    #print(count0,count1,count2)
    
    complexity = O(n)
 
 
    
 
