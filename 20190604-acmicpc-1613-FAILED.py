## problem source :https://www.acmicpc.net/problem/1613
## Unsolved : 2019 - 06 - 04 (Tue)

## 기본적인 알고리즘 공부하고 풀자..
## 그 다음에 적용..
import sys
from copy import deepcopy
## n= 사건의 개수(1~500), k 전후관계 개수(1~50,000)
## 사건의 이름 == 숫자, 그러나 str이다!
## git의 push, merge 같은 느낌..!!

def save(n):
    if(direct_merge(n)):
        return
    tree.append([n[0],n[1]])

def small():
    del_li=[]
    for x in range(len(tree)-1):
        for y in range(x,len(tree)):
            if(len(tree[x])<len(tree[y])):
                t=len(tree[x])
                for j in tree[x]:
                    if(j not in tree[y]):
                        break
                    else:
                        t-=1
                if not t:
                    del_li.append(x)
            if(len(tree[y])<len(tree[x])):
                t=len(tree[y])
                for j in tree[y]:
                    if(j not in tree[x]):
                        break
                    else:
                        t-=1
                if not t:
                    del_li.append(y)

    for n,x in enumerate(del_li):
        del tree[x-n]

def direct_merge(n):
    for x in tree:
        if(x[-1]==n[0]):
            x.extend(n[1])
            return 1
    return 0

def pull_request():
    requests=[]
    for x in range(len(tree)):
        for y in range(x+1,len(tree)):
            if(tree[x][0]==tree[y][1]):
                requests.append((y,x))
            if(tree[y][0]==tree[x][1]):
                requests.append((x,y))
    # 인덱스는 절대 안 겹치고, 방향성이 존재하기 때문에 set(교집합) 할 필요 x
    return requests

def merge(n):
    del_li=[]
    # 인덱스가 작은 순으로 먼저 적용된다는 점!
    for x in n:
        # 병합하는 정보의 인덱스
        # 이미 앞 인덱스가 병합된 상태면 pass
            if(len(tree[x[0]])!=2):
                continue
            else:
                # tree[x[0]].extend(deepcopy(tree[x[1]][1:] ))
                tree[x[0]].extend(tree[x[1]][1:])
                del_li.append(x[1])
    if(len(del_li)==0):
        return 0
    for n,x in enumerate(del_li):
        del tree[x-n]
    return 1

def read(k):
    t=1
    for i in range(1,k+1):
        if(i%5==0):
        # if(i):
            save(sys.stdin.readline().split())
            sys.stdin.flush()
            small()
            while(t):
                t =merge(pull_request())
        else:
            save(sys.stdin.readline().split())
            sys.stdin.flush()
    small()
    while(t):
        t =merge(pull_request())

def search(k):
    for _ in range(k):
        n,m =map(str, sys.stdin.readline().strip().split())
        for branch in tree:
            if(n not in branch or m not in branch):
                li.append(0)
                continue
            li.append( -1 if branch.index(n) < branch.index(m) else 1)

if __name__=='__main__':
    tree=[]; li=[]
    n,k =map(int, sys.stdin.readline().strip().split())
    read(k)
    k = int(sys.stdin.readline())
    search(k)
    for x in li:
        print(x)
