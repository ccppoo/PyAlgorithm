## problem source : https://www.acmicpc.net/problem/2577
## Unsolved : 2019 - 06 - 05 (Wend)
import sys
import math
n=1
for _ in range(3):
    n *=int(sys.stdin.readline())
n=list(str(n))
num=[0,0,0,0,0,0,0,0,0,0]
for x in n:
    num[int(x)]+=1
for s in num:
    print(s)
