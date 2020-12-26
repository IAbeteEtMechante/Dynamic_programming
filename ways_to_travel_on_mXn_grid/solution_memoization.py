from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
import sys  
input=sys.stdin.readline
 
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))

m, n = rl()

dp =  [[-1] * n for _ in range(m)]

dp[m-1][n-1] = 1

def solve(i,j):
	if dp[i][j] != -1:
		return dp[i][j]
	else:
		dp[i][j] = 0
		if i + 1 < m:
			dp[i][j] += solve(i+1,j)
		if j+1 < n:
			dp[i][j] += solve(i,j+1)
	return dp[i][j]
 

print(solve(0,0))