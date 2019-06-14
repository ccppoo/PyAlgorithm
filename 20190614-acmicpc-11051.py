## problem source :https://www.acmicpc.net/problem/11051
## Unsolved : 2019 - 06 - 11 (Tue )
import sys

# hocky stick
if __name__=='__main__':

    def nCm(n,m):
        ak=1
        if(m>n//2):
            m=n-m
        for x in range(n-m+1, n+1):
            ak*=x
        for k in range(1,m+1):
            ak//=k
        return ak

    n,m =map(int, sys.stdin.readline().split())
    n-=1; m-=1
    an=0
    if(n<1 or m<0):
        print(1)
        exit()
    while(n!=m):
        an+=nCm(n,m)
        if(an>=10007):
            an =an%10007
        n-=1
    print((an+1)%10007)
