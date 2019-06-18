## problem source : https://www.acmicpc.net/problem/6064
## Unsolved : 2019 - 06 - 18 (Tue)
'''
달력 x:y
입력 a:b
abs(y-x) 주기 (여분 y%x)
a:b = a가 가지는 lhs의 종류 :
x:x에서  다음줄 --> x:(x+y)%y
        다음줄 --> x:(x*2+y)%y 만약 나머지 0이면 y
        다음줄 --> x:(x*3+y)%y
        '''
import sys
def sol_1(k):
    cnt=k[2]
    lines=1
    t=0
    if(k[2]==k[3]):
        return k[3]
    while((k[0]*lines+k[1])%k[1]!=0):
        lines+=1
    # print('lines',lines)
    if(lines==1):
        if(cnt==k[3]):
            return cnt
    if(k[3]==k[1]):
        for x in range(1,lines):
            cnt+=k[0]
            # print('cnt :',cnt)
            if(cnt%k[1]==0):
                return cnt
    else:
        for x in range(1,lines):
            cnt+=k[0]
            # print('cnt :',cnt)
            if(cnt%k[1]==k[3]):
                return cnt

    return -1

for _ in range(int(input())):
    k=list(map(int, sys.stdin.readline().split()))
    if(k[0]<=k[1]):
        print(sol_1(k))
    else:
        print(sol_1([k[1],k[0],k[3],k[2]]))
