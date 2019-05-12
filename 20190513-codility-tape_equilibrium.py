## problem source : https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
## Unsolved : 2019 - 05 -13 (Mon) 2:30 AM
## reminds me of gradient descent, getting Global minima
## First time of using codility, so I couldn't get evaluation of my codes

##  실수 단위가 아니라 인덱스 별로 값이 존재하기 때문에,
##  평균으로부터 제일 가까운 값을 구하면, 그것이 나눈 리스트의 합의 차의 최소다
##  지난 cookie 문제와 달리, 최솟값만 구하면 되므로 0을 갖는 인덱스가 나와도
##  어차피 두 리스트 합의 차 최솟값은 0이니깐 상관없다, 다만 중복될 수 있을뿐

## 랜덤으로 10만개의 인덱스 리스트를 생성해도 5~6초 소요... 이 정도면 충분하겠지?

from time import time
import random

'''
배열 크기 : 2~100,000
각 원소의 크기 : -1,000 ~ 1,000
'''
def solution(cookie):
    hap  = sum(cookie)
    length = len(cookie)
    ave = int(hap/length)
    i = 1; lhs  =cookie[0]
    flag = []
    while(i<length-1):
        lhs +=cookie[i]
        if( (lhs>ave-1000) or (lhs<ave+1000)):
            rhs = hap-lhs
            print(abs(lhs-rhs))
            flag.append(abs(lhs-rhs))
        i+=1

    if len(flag)>1:
        return min(flag)
    else:
        # 계속 증가, 감소하는 경우
        return flag[0]

if __name__=='__main__':
    list_test =[]
    for _ in range(0,100000):
        list_test.append(random.randint(-1000,1000))
    # list_test = [3,1,2,4,3]
    # 결과값  : 1
    print('길이', len(list_test))
    print("시작")
    start_time = time()
    print('답', solution(list_test))
    print("--- %s seconds ---" %(time() - start_time))
