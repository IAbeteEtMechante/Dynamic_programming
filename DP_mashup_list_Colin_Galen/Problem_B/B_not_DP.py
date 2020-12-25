from collections import *
import sys  
import string
input=sys.stdin.readline

# "". join(strings)  
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))
    
n, k = rl()
ss = input()
cc = input().split()
# print(cc)

alphabet = string.ascii_lowercase

# print(alphabet)

missing = ""
for letter in alphabet:
	if letter not in cc:
		missing += letter

# print(missing)

for letter in missing:
	ss = ss.replace(letter, " ")

ans = 0
for group in ss.split():
	k = len(group)
	ans += k*(k + 1) // 2

print(ans)