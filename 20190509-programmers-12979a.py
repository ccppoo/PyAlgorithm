def solution(n, stations, w):
    temp =1
    answer =0
    '''
    n = 아파트의 개수 int
    stations = 기지국의 개수 1차원 배열 [] + 오름차순
    w = 전파거리 int
    리턴값 : 최소 기지국 개수

    주어진 w에 따라서 최소 1+2w 만큼의 빈공간 커버 가능
    기지국 위치에서 전파가 닿은곳+-1 만큼의 인덱스를 추려냄
    '''
    # 주어진 거리에서 설치해야되는 최소 기지국 개수 리턴
    # lhs = 왼쪽 지점(없는 지역부터), rhs = 오른쪽 지점(없는 지역까지), w= 전파 수신거리
    def getS(lhs, rhs, w):
        if(lhs==rhs):
            return 1
        # 전파가 안닿는 거리 : rhs-lhs+1
        # 방법 1 :
        # Ntemp += (rhs-lhs+1) // (2*w+1)
        # Ntemp += 1 if ((rhs-lhs+1) % (2*w+1)>0) else 0
        # 방법 2 :
        Ntemp, Dtemp = divmod((rhs-lhs+1),(2*w+1))
        Ntemp += 1 if Dtemp >0 else 0

        return Ntemp


    for x in stations:
        #### 첫번째 노드에만 해당
        if(x-w <=1):
            temp = x+w
            continue
        elif temp==1:
            # x-w !=0 그러나 처음(temp =0)
            answer += getS(1,x-w-1, w)
            temp = x+w
            continue

        #### 두번째 노드부터 해당
        if(temp >= x-w -1):
            #다음 기지국의 망이 걸치는 경우 + 딱 들어맞는 경우(-1)
            temp = x+w
            #다음의 기지국 전파 닿는 거리로 갱신
            continue
        else:
            #다음 기지국의 망이 안 걸치는 경우
            answer += getS(temp+1, x-w-1, w).
            temp = x+w
        if(temp>n):
            return answer
    ##### 모든 기지국 다 for 문 돌고 마지막에 temp = x+w 갱신됨
.
    if(temp<n):
        #최우축의 기지국의 전파가 마지막 아파트에 안닿는 경우
        answer += getS(temp+1, n, w)
    # else:
        #최우축의 기지국의 전파가 마지막 아파트에 안닿는 경우
        #또는 그 이상 넘어가는 경우 아무것도 안해도됨

    return answer

if __name__=='__main__':
     i = solution(11, [4,11], 1)
     print("정답", i)
