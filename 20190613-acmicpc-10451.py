## problem source : https://www.acmicpc.net/problem/10451
## solved : 2019 - 06 - 13 (Thur)
## TOO SLOW

from sys import stdin
import sys
sys.setrecursionlimit(2000)
def doit():
    size =int(stdin.readline())
    li=list((map(int, stdin.readline().split())))
    # track = 인덱스
    def search(track, stack,start=None):
        if(start!=None):
            # print('첫 시작 : ', start,'index stacks :',stack)
            # 이상적인 고리
            li[stack[0]]
            li[track]
            if(li[stack[0]] ==li[track]):
                # print('정상 고리 ')
                return stack,1
            # 밖에서 끼어든 순환의 경우(b 같이 생긴 고리)
            # 여기서 거르지 않아도 알아서 카운트 됨
            if(track in stack):
                # print('비정상 고리 ')
                return stack[:t+1], 0
            stack.append(track)
            return search(li[track]-1,stack, start)
        else:
            print('시작!!', 'start index:', track,'start value : ', li[track])
            stack.append(track)
            return search(li[track]-1, stack,track)

    cycle=0

    li_2=[x for x in range(len(li))]
    while(li_2):
        indice, n= search(li_2[0],[])
        if(n):
            print('cycle(indice) :',indice)
            cycle+=1
        print('제거하는 인덱스들 :',indice)
        for k in indice:
            li_2.remove(k)
    print(cycle)

if __name__=='__main__':
    n= int(stdin.readline())
    for _ in range(n):
        doit()
