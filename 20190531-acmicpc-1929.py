## problem source : https://www.acmicpc.net/problem/1929
## Unsolved : 2019 - 05 -31 (Fri)

## Getting prime numbers

## 출력은 숫자하나씩 출력 print()

import sys
from math import sqrt

n, m =sys.stdin.readline().split()
n =int(n); m =int(m)
li =[x for x in range(2,m+1) if x%2!=0 or x%3!=0]
net = [x for x in range(2, int(sqrt(m))+1)]
for x in [x for x in range(2, int(sqrt(m))+1)]:
    net = [k for k in net if k%x!=0 or k==x]
for x in net:
    li = [k for k in li if k%x!=0 or k==x]
li =[x for x in li if x>=n and x<=m]
print(len(li))
for x in li:
    print(x)
