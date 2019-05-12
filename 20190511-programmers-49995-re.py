## problem source : https://programmers.co.kr/learn/courses/30/lessons/49995
## Unsolved : 2019 - 05 -11 (Sat) ~ ...
## it's not about programming, it's mathmatic sense
## Version re : just acknowlodgement of problem and finding a way


##  차례대로 더하고 넘긴 구간 내에서 구간합의 반이 되면 그 값을 리턴(형과 동생이 같은 개수)
##  정확성 테스트 : clear
##  효율성 테스트 : 3,4,5,7

from copy import deepcopy
from time import time

def solution(cookie):

    def sum_check(start, end, curr_max):
        if(start==0):
            range_sum = cookie[end]
            half = range_sum//2
            while(range_sum>half):
                range_sum -= cookie_origin[start]
                start+=1
            if(range_sum==half and range_sum>curr_max):
                return half
            else:
                return curr_max
        else:
            range_sum = cookie[end] -cookie[start-1]
            half = range_sum//2
            while(range_sum>half):
                range_sum -= cookie_origin[start]
                start+=1
            if(range_sum==half and range_sum>curr_max):
                return half
            else:
                return curr_max

    max =0
    cookie_origin = deepcopy(cookie)
    # 각 바구니(리스트 각각의 인덱스 내용)에는 최소 1개의 과자가 있음
    # 즉, 기울기 0초과하는 선형 증가함수임, 직각 삼각형이라고 생각하면 됨
    for i in range(1, len(cookie)):
        cookie[i] = cookie[i] + cookie[i-1]

    # cookie[start] ~ end[cookie] 짝수면 무조건 반토막 가능(증가함수 + 자연수 만큼 증가)
    for end in range(1 , len(cookie)):
        temp = cookie[end]
        if(temp%2 ==0):
            max = sum_check(start = 0, end = end, curr_max=max)
            if(max ==cookie[-1]//2):
                return max

    for start in range(1, len(cookie)-1):
        for end in range(start+1 , len(cookie)):
            temp = cookie[end] -cookie[start-1]
            if(temp%2 ==0):
                max = sum_check(start=start, end=end, curr_max=max)
                if(max ==cookie[-1]//2):
                    return max

    return max


if __name__=='__main__':
    # list_test = [x for x in range(0,500)]*4
    list_test = [500]*2000
    print(len(list_test))
    print("시작")
    start_time = time()
    print(solution(list_test))
    print("--- %s seconds ---" %(time() - start_time))
