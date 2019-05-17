## problem source : https://www.acmicpc.net/problem/1074
## Unsolved : 2019 - 05 -17 (Fri)

## 이 문제는 배열을 생성하고 직접 찾아가는 것이 아닌, 패턴대로 푼 것
## 배열을 생성할 경우, 최대 2^16 개의 원소를 갖는 배열을 요구하므로(대충 생각하면)
## 알고리즘이라고 부를 가치가 없음

## 입력값을 어떻게 준다는건데 ???


'''(r, c) == (행, 열)'''
# total : 2^N * 2^N = 2*(N+1) numbers
'''
top_left = 2**n 개 각각 있음!
top_right =
bottom_left =
bottom_right =
Z를 그리면서 카운트하는 패턴은 크던 작던 동일함
이를 단지 크게 놓고보면 탐색범위를 기하급수적으로 줄일 수 있음
이 풀이에서는 좌표를 0이 아닌, 1부터 시작할거임
여기서 말하는 사분면(quadrant)는 일반적인 사분면이 아닌, Z 방향 순으로
1  2
3  4 임
'''
def get_quadrant(N, r, c):
    if(N == 0):
        return 0
    if(r <= 2**(N-1)):
        if(c <=2**(N-1)):
            return 1
        else:
            return 2
    else :
        if(c <=2**(N-1)):
            return 3
        else:
            return 4

def solution(N, r, c):
    answer = 0

    ## 1.
    quad = get_quadrant(N, r, c)
    r +=1; c+=1
    flag = 123
    while(flag):
        # print('N : '+str(N) +' r : '+str(r)+ ' c : '+str(c))
        flag = get_quadrant(N,r,c)
        # print('FLAG : ', flag)
        if(flag):

            # print('2**(n-1) : '+str(2**(N-1)) + ' ,Flag -1 : '+str(flag-1), end='\n\n')
            print('★작은 사분면 개수  : ', (2**(N-1))**2, ' 나머지 사분면 :', (flag-1), '    N =', N)
            print('☆이거 더함 : ',  ((2**(N-1))**2)*(flag-1), end='\n\n')
            answer += ((2**(N-1))**2)*(flag-1)
            if(flag ==1):
                r=r; c=c
            elif(flag ==2):
                r=r; c = c - 2**(N-1)
            elif(flag ==3):
                r =  r -2**(N-1); c = c
            elif(flag ==4):
                r = r -2**(N-1); c= c - 2**(N-1)
        N -=1

    print(answer)

if __name__ =='__main__':
    solution(2,3,1)
    print('Answer : 11')
    solution(3,7,7)
    print('Answer : 63')
