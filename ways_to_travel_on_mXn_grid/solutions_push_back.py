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

dp =  [[0] * n for _ in range(m)]

dp[m-1][n-1] = 1

for j in range(n-1, -1, -1):
	for i in range(m - 1, -1, -1):
		if j - 1 >= 0:
			dp[i][j- 1] += dp[i][j]
		if i - 1 >= 0:
			dp[i - 1][j] += dp[i][j]
print(dp[0][0])