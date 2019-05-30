## problem source : https://www.acmicpc.net/problem/2775
## Unsolved : 2019 - 05 -30 (Fri)

##
'''이 아파트에 거주를 하려면 조건이 있는데,
“a층의 b호에 살려면 자신의 아래(a-1)층의
1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는
계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고
모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
주어지는 양의 정수 k와 n에 대해 k층에 n호에는
몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.'''
import sys

n =sys.stdin.readline()

'''아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.'''
class apt:
    def __init__(self, floor, num):
        self.floor = floor
        self.num =num
        self.flr =[ [x for x in range(1,num+1)]]
        self.ans =0

    def count(self):
        for x in range(self.floor):
            temp =[ sum(self.flr[x][0:y+1]) for y in range(self.num)]
            self.flr.append(temp)
        self.ans = self.flr[self.floor][self.num-1]

    def answer(self):
        print(self.ans)

for _ in range(int(n)):
    i =int(sys.stdin.readline())
    j =int(sys.stdin.readline())
    k =apt(i,j)
    k.count()
    k.answer()











#
