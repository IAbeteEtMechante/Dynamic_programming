#based on jimm89
from collections import *
import sys  
input=sys.stdin.readline

N = 75
INF = 10**18

# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))



"""
For each of the first i rows, find the maximum sum for each value mod K
Precompute these
Then cycle through
Maximum sum of X elements equal to J mod K = maximum sum of X-1 elements equal to
 
 
"""
 
def solve():
    N, M, K = rl()
    S = []
    for n in range(N):
        S.append(rl())
    tmp = []
    for n in range(N):
        #each value mod K, up to m elements
        dp = [[-INF for k in range(K)] for m in range(M//2+1)]
        #empty set
        dp[0][0] = 0
        for m in range(M):
            for m2 in range(M//2-1,-1,-1):
                for k in range(K):
                    dp[m2+1][(k+S[n][m])%K] = max(dp[m2+1][(k+S[n][m])%K], dp[m2][k] + S[n][m])
    
        dp2 = [-INF]*K
        for m2 in range(M//2+1):
            for k in range(K):
                dp2[k] = max(dp2[k],dp[m2][k])
        
        tmp.append(dp2)
 
    ans = list(tmp[0])
    
    for n in range(1,N):
        curr = list(tmp[n])
        tmp2 = [-10**18]*K
        for k1 in range(K):
            for k2 in range(K):
                tmp2[(k1+k2)%K] = max(tmp2[(k1+k2)%K], curr[k1]+ans[k2])
        ans = list(tmp2)
    
    return ans[0]

print(solve())