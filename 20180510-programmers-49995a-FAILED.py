## problem source : https://programmers.co.kr/learn/courses/30/lessons/49995
## Unsolved : 2019 - 05 -10 (Fir) ~ ...
## Can't Find more better time complexity than O(n^3)
## Version a : sending parameters as index and referencing the original list

##  서치할 구간의 인덱스를 넘기고 cookie의 리스트를 참조함
##  시간초과 : 6,7,8,9, 23, 26
##  효율성 테스트 : x
import time

def solution(cookie):
    hap = sum(cookie)
    gily = len(cookie)
    max = 0

    def sum_check(a,b):
        temp = 0
        ''' 아래와 같이 따로 만든 이유는 주어진 인덱스 구간을 반복적으로 나눠서 합산할 떄
            sum 매소드가 이터레이터만 가능한데, (1개 vs 나머지 합)의 경우 신텍스 에러 발생
        '''
        if(a-b == 1):
            t = cookie[a]
            k = cookie[b]
            if( t== k):
                temp = temp if temp > t else t
            return temp

        elif(a-b ==2):
            # t = sum(cookie[a:a+2])
            t = cookie[a] + cookie[a+1]
            k = cookie[b]
            if( t== k):
                temp = temp if temp > t else t
            t = cookie[a]
            t = cookie[b-1] + cookie[b]
            if( t== k):
                temp = temp if temp > t else t
            return temp

        else:
            for b_start in range(a+1, b+1):
                #하나 vs 나머지
                if (a+1 == b_start) :
                    t = cookie[a]
                    k = sum(cookie[b_start:b+1])
                    if( t== k):
                        temp = temp if temp > t else t
                    continue

                #나머지 vs 두개
                if (b-b_start== 1) :
                    t = sum(cookie[a:b_start])
                    k = cookie[b_start] + cookie[b]
                    if( t== k):
                        temp = temp if temp > t else t
                    continue

                #나머지 vs 하나
                if (b==b_start) :
                    t = sum(cookie[a:b])
                    k = cookie[b]
                    if( t== k):
                        temp = temp if temp > t else t
                    return temp

                t = sum(cookie[a:b_start])
                k = sum(cookie[b_start:b+1])
                if( t== k):
                    temp = temp if temp > t else t


        return temp

    for i in range(0,gily):
        for j in range(i+1, gily):
            print('\n인덱스 i 부터 j 까지 : ', i,'~', j)
            temp = sum_check(i,j)
            # # TODO: 인덱스 대신에 잘라낸 리스트 넘기기
            max = max if max > temp else temp

    return max

if __name__=='__main__':
    list_test = [x for x in range(0,200) ]
    print(len(list_test))

    print("시작")
    start_time = time.time()
    print(solution(list_test))
    print("--- %s seconds ---" %(time.time() - start_time))
