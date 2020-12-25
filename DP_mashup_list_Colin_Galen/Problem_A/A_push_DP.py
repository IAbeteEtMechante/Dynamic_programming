from collections import *
import sys  
input=sys.stdin.readline

N = 60

# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))

n = ri()
    
#state is just an integer
dp = [0] * (N + 5)  #5 is just add ourselves some margin

#base cases
dp[0] = 0
dp[1] = 0
dp[2] = 2

#transitions (push)
for i in range(n):
	dp[i + 2] += 2*dp[i]

print(dp[n])

