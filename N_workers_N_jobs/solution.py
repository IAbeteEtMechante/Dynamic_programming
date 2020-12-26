#inspired from https://www.youtube.com/watch?v=685x-rzOIlY&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=3

from collections import *
import sys  
input=sys.stdin.readline


# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))
    
n = ri()
A = []

for _ in range(n):
	#each row correspond to one job
	A.append(rl())
	#each column of the matrix correspond to one worker

#brute force would be n!

#dp(i , mask) = minimum cost to assign people from the mask to jobs i -> n  (assign n - i + 1 jobs to n - i people from the mask)
#mask is a subset of {P1, P2, ...Pn} of size n - i + 1
#mask has n bits. If kth bit is on, Pk is in the mask  

#answer will be dp(1, 1111....11)

#space complexity: n * 2^n

#time complexity: n^2 * 2^n 


dp = [[10**18]* 2**22 for _ in range(22)]


def solve(i, mask, n):
	#n is in the function just to know when to stop (base case)
	if i == n - 1:
		for k in range(n):
			if mask & (1 << k):
				dp[i][mask] = A[i][k]
				return dp[i][mask]
	else:
		if dp[i][mask] != 10**18:
			return dp[i][mask]
		else:
			#for each bit in the mask, we try to affect Ji to that the worker corresponding to that bit
			for k in range(n):
				if mask & (1 << k):
					dp[i][mask] = min(A[i][k] + solve(i + 1, mask & ~(1 << k), n), dp[i][mask])
			return dp[i][mask]
print(solve(0,2**n - 1, n))



