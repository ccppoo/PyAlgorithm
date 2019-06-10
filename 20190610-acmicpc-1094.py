## problem source : https://www.acmicpc.net/problem/1094
## solved : 2019 - 06 - 10 (Mon)
from sys import stdin
print(list(bin(int(stdin.readline()))).count('1'))
