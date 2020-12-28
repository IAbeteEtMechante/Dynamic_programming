from collections import *
import sys  
import string
from math import inf

N = 1000

input=sys.stdin.readline


# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))
    
n = ri()
pp = []
vv = []
for i in range(n):
	price, vitamins = input().split()
	pp.append(int(price))
	vv.append(vitamins)

#dp = [juice i][maskVitamins] = min price to pay if we can chose within i-1 first juices to have the vitamins in the mask

#this is the same as the dp in the other solution, except that we regroup all the dps into one big matrix
dp = [[inf] * 8 for i in range((N + 5))]

#base case:

#create a bitmask from the juice
juice_mask = 0
if "C" in vv[0]:
	juice_mask += 1 
if "B" in vv[0]:
	juice_mask += 2 	
if "A" in vv[0]:
	juice_mask += 4
for mask in range(8):
	if mask & juice_mask == mask:
		dp[0][mask] = pp[0]


#transitions:
for i in range(n - 1):

	#create a bitmask from the juice
	juice_mask = 0
	if "C" in vv[i + 1]:
		juice_mask += 1 
	if "B" in vv[i + 1]:
		juice_mask += 2 
	if "A" in vv[i + 1]:
		juice_mask += 4

	for mask in range(8):
		#if we want, we dont take the juice at rank i + 1
		dp[i + 1][mask] = min(dp[i][mask], dp[i + 1][mask])

		#we can also chose to only take the juice at i + 1:
		if mask & juice_mask == mask:
			dp[i + 1][mask] = min(pp[i+1], dp[i + 1][mask])

		#or we take a mix
		dp[i + 1][mask | juice_mask] = min(dp[i][mask] + pp[i + 1], dp[i + 1][mask | juice_mask])

ans = dp[n - 1][7]

if ans == inf:
	print(-1)
else:
	print(ans)













