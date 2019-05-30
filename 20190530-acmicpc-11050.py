import sys
n,m =sys.stdin.readline().split()
k=1
s =[x for x in range(int(n)+1-int(m), int(n)+1)]
q =[x for x in range(1,int(m)+1)]
for x in s:
    k*=x
for x in q:
    k= k//x
print(k)
