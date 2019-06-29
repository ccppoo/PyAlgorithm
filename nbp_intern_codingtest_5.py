def solution(X):
    # 주어진 배열에서 A[a] , A[b]가 있다면
    # 도시의 인덱스 abs(a-b) + a +b에서 최대 구하는 것
    # 걸리는 계산 nC2 + 모두 비교하는 시간 n = n^2
    king=[]
    for s in range(len(A)):
        temp=[]
        for e in range(len(A)):
            temp.append(abs(s-e)+X[e]+X[s])
        king.append(max(temp))
    return max(king)

if __name__=='__main__':
    A=[-8, 4, 0, 5, -3, 6]
    print(solution(A), 'Answer should be :',14)
