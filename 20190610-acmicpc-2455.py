## problem source : https://www.acmicpc.net/problem/2455
## solved : 2019 - 06 - 10 (Mon)
from sys import stdin

li=[]
for i in range(4):
    n,m=map(int, stdin.readline().split())
    if(li):
        li.append(li[i-1]+m-n)
    else:
        li.append(m-n)
print(max(li))
