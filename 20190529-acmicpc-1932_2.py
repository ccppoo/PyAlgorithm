## problem source : https://www.acmicpc.net/problem/1932
## Unsolved : 2019 - 05 -28 (Tue)

## Olympiad > International Olympiad in Informatics > IOI 1994 problem 1
## number triangle
## 삼각형 크기 1~500, 정수 범위 0~9999

## 문제 형식을 바꾸기 싫다면서 (경로)출력은 그리디??
from copy import deepcopy
def main():
    import sys

    size_tri = int(sys.stdin.readline())
    pyramid =[]
    for _ in range(size_tri):
        pyramid.append([[n,int(x)] for n,x in enumerate(sys.stdin.readline().strip().split())])

    ## input 1, 1 2, 1 2 3
    '''
    첫번째가 좌표, [전체 [ 층  [ 층 마다 원소(좌표, 값)  ]]]
    pyramid = [ [[0, 1]],
                [[0, 1], [1, 2]],
                [[0, 1], [1, 2], [2, 3]]
    ]
    '''
    # 좌표가 같은 값 중에서 value가 큰것만 남기기
    def cmp(curr):
        # 최대 연산수 499*500/2번이므로 최적화 하자
        '''
        양끝 하나를 제외한 2개 반복 : 0,1,2,3  1,2,3,4
        '''
        hf = int(len(curr)/2)
        for x in range(1,hf):
            # print('비교:',curr[x], curr[len(curr)-x-1])
            if(curr[x] < curr[x+hf-1]):
                curr[x] = curr[x+hf-1]
        for _ in range(hf-1):
            curr.pop(-2)

    curr =[x for x in pyramid[0]] # 구할 다음 층의 합 저장하는 리스트 (합이 같은 경우도 있으므로 리스트안에 리스트)
    '''첫번째 curr : [[0, 1]] '''
    depth =0
    size_tri -=1
    # 왼쪽 대각선, 오른쪽 대각선 vs 왼쪽 대각선, ... , 오른쪽 대각선
    # 계산횟수는 각 층의 개수(n)이면 n*2회
    while(depth<size_tri):
        depth+=1
        # 단순한 복사를 하는 경우 리스트([ ])를 복사하는 것이기 때문에, 주소가 연동된다(shallow copy).
        curr = curr+deepcopy(curr)
        half = int(len(curr)/2)
        for x in range(half):
            # print(depth,'층',pyramid[depth])
            # 왼쪽 대각선
            curr[x][1] +=pyramid[depth][x][1]
            # curr[x][0] = curr[x][0] + 0 좌표는 그대로

            # 오른쪽 대각선
            curr[x+half][1]
            pyramid[depth][x+1][1]
            curr[x+half][1] +=pyramid[depth][x+1][1]
            # 오른쪽 대각선으로 이동,  좌표 +1
            curr[x+half][0] +=1
        ## 같은 좌표 ( 왼쪽 대각선 , 오른쪽 대각선 만나는 곳) 더 큰 값만 추려내기
        cmp(curr)


    max=0
    # curr = [x[1] for x in curr]
    # print(curr)
    for x in curr:
        if(max <x[1]):
            max=x[1]
    print(max)

if __name__=='__main__':
    main()
#
