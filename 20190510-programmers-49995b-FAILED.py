## problem source : https://programmers.co.kr/learn/courses/30/lessons/49995
## Unsolved : 2019 - 05 -10 (Fir) ~ ...
## Can't Find more better time complexity than O(n^3)
## Version b : sending parameters as slice of list (between searching indice)


##  서치할 구간을 인덱싱을 한 후에 대입함
##  시간초과 : 6,7,8,9, 23, 26
##  효율성 테스트 : x
import time

def solution(cookie):
    gily = len(cookie)
    max = 0

    def sum_check(temp_list, a, b):
        # print('a : ', a, 'b : ',b )
        temp = 0
        list_sum_half = sum(temp_list)
        ''' 아래와 같이 따로 만든 이유는 주어진 인덱스 구간을 반복적으로 나눠서 합산할 떄
            sum 매소드가 이터레이터만 가능한데, (1개 vs 나머지 합)의 경우 신텍스 에러 발생
        '''
        if(a-b == 1):
            t = temp_list[a]
            k = temp_list[b]
            if( t== k):
                temp = temp if temp > t else t
            return temp

        elif(a-b ==2):
            # t = sum(cookie[a:a+2])
            t = temp_list[a] + temp_list[a+1]
            k = temp_list[b]
            if( t== k):
                temp = temp if temp > t else t
            t = temp_list[a]
            t = temp_list[b-1] + temp_list[b]
            if( t== k):
                temp = temp if temp > t else t
            return temp


        for b_start in range(a+1, b+1):
            #하나 vs 나머지
            if (a+1 == b_start) :
                t = temp_list[a]
                if(t>list_sum_half):
                    continue
                elif(t==list_sum_half):
                    temp = t
                    continue

                k = sum(temp_list[b_start:b+1])
                if( t== k):
                    temp = temp if temp > t else t
                continue

            #나머지 vs 두개
            if (b-b_start== 1) :
                k = temp_list[b_start] + temp_list[b]
                if(k>list_sum_half):
                    continue
                elif(k==list_sum_half):
                    temp = k
                    continue

                t = sum(temp_list[a:b_start])
                if( t== k):
                    temp = temp if temp > t else t
                continue

            #나머지 vs 하나
            if (b==b_start) :
                k = temp_list[b]
                if(k>list_sum_half):
                    continue
                elif(k==list_sum_half):
                    temp = k
                    continue
                t = sum(temp_list[a:b])
                # print('문제 : ', b, 'temp_list : ',temp_list)
                if( t== k):
                    temp = temp if temp > t else t
                return temp

            t = sum(temp_list[a:b_start])
            if(t>list_sum_half):
                continue
            elif(t==list_sum_half):
                temp = t
                continue
            k = sum(temp_list[b_start:b+1])
            if( t== k):
                temp = temp if temp > t else t
        del temp_list
        #for -loop 종료


        return temp

    for i in range(0,gily):
        for j in range(i+1, gily):
            # print('i : ', i,'j : ',j)
            temp = sum_check(cookie[i:j+1], 0, j-i)
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
