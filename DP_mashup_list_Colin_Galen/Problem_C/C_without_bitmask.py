from collections import *
import sys  
import string

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


ABC = [10**9] * (N + 5)
AB = [10**9] * (N + 5)
BC = [10**9] * (N + 5)
CA = [10**9] * (N + 5)
A = [10**9] * (N + 5)
B = [10**9] * (N + 5)
C = [10**9] * (N + 5)

#base case
if "A" in vv[0]:
	A[0] = pp[0]
if "B" in vv[0]:
	B[0] = pp[0]
if "C" in vv[0]:
	C[0] = pp[0]
if "A" in vv[0] and "B" in vv[0]:
	AB[0] = pp[0]
if "A" in vv[0] and "C" in vv[0]:
	CA[0] = pp[0]
if "B" in vv[0] and "C" in vv[0]:
	BC[0] = pp[0]
if "B" in vv[0] and "C" in vv[0] and "A" in vv[0]:
	ABC[0] = pp[0]


#transitions:
for i in range(n - 1):
	A[i + 1] = A[i]
	if "A" in vv[i + 1]:
		A[i + 1] = min(pp[i + 1], A[i + 1])

	B[i + 1] = B[i]
	if "B" in vv[i + 1]:
		B[i + 1] = min(pp[i + 1], B[i + 1])

	C[i + 1] = C[i]
	if "C" in vv[i + 1]:
		C[i + 1] = min(pp[i + 1], C[i + 1])

	AB[i + 1] = AB[i]
	if "A" in vv[i + 1]:
		AB[i + 1] = min(pp[i + 1] + B[i], AB[i + 1])
	if "B" in vv[i + 1]:
		AB[i + 1] = min(pp[i + 1] + A[i], AB[i + 1])
	if "A" in vv[i + 1] and "B" in vv[i + 1]:
		AB[i + 1] = min(pp[i + 1], AB[i + 1])

	BC[i + 1] = BC[i]
	if "C" in vv[i + 1]:
		BC[i + 1] = min(pp[i + 1] + B[i], BC[i + 1])
	if "B" in vv[i + 1]:
		BC[i + 1] = min(pp[i + 1] + C[i], BC[i + 1])
	if "C" in vv[i + 1] and "B" in vv[i + 1]:
		BC[i + 1] = min(pp[i + 1], BC[i + 1])

	CA[i + 1] = CA[i]
	if "C" in vv[i + 1]:
		CA[i + 1] = min(pp[i + 1] + A[i], CA[i + 1])
	if "B" in vv[i + 1]:
		CA[i + 1] = min(pp[i + 1] + C[i], CA[i + 1])
	if "C" in vv[i + 1] and "A" in vv[i + 1]:
		CA[i + 1] = min(pp[i + 1], CA[i + 1])


	ABC[i + 1] = ABC[i]
	if "A" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + BC[i], ABC[i + 1])
	if "B" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + CA[i], ABC[i + 1])
	if "C" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + AB[i], ABC[i + 1])

	if "A" in vv[i + 1] and "B" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + C[i], ABC[i + 1])
	if "A" in vv[i + 1] and "C" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + B[i], ABC[i + 1])
	if "C" in vv[i + 1] and "B" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1] + A[i], ABC[i + 1])

	if "A" in vv[i + 1] and "B" in vv[i + 1] and "C" in vv[i + 1]:
		ABC[i + 1] = min(pp[i + 1], ABC[i + 1])

ans = ABC[n - 1]
if ABC[n - 1] == 10**9:
	ans = -1
print(ans)