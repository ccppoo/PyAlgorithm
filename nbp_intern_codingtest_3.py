
# 인덱스간 거리가 100,000,000 보다 크면 -1 인덱스간 거리  : abs(A[a]-A[b])
# 인접인덱스가 없으면 -2 (모든 수가 같은 경우?)
# 아니면 최소 거리 min, list of abs(A[a]-A[b])

def solution(A):
    A.sort()
    if(len(set(A))==len(A)):
        return 0
    elif(len(set(A))==1):
        return -2
    if(A[-1]-A[0]>100000000):
        return -1
    li=[]
    for i in range(len(A)-1):
        li.append(A[i+1]-A[i])
    return min(li)

if __name__=='__main__':
    print(solution([0,3,3,7,5,3,11,1]))
