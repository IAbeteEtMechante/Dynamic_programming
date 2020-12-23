from collections import *
import sys  
import string

N = 200000

input=sys.stdin.readline



# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))
    
n, k = rl()
ss = input()
cc = input().split()

#state: just position in the string is not working

#we need to fix something more to define the state
#dp = number of substring finishing exactly at ith position
dp = [0] * (N + 5)

if ss[0] in cc:
	dp[0] = 1
else:
	dp[0] = 0

for i in range(n):
	if ss[i + 1] in cc:
		dp[i + 1] = 1 + dp[i]

ans = sum(dp[:n])
print(ans)



