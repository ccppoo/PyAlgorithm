## problem source : https://programmers.co.kr/learn/courses/30/lessons/42626
## Unsolved : 2019 - 05 -24 (Fri)

## level 2 problem in programmers
## 문제 만든 사람이 3,3,5가 있으면 3이 제일 작고, 3도 2번째로 작은 숫자랜다...ㅋㅋ
## https://programmers.co.kr/learn/questions/3905

'''섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수
                        + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

    Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
scoville의 길이는 1 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
'''
def solution(scoville, K):
    # print('시작 : ', scoville)
    answer = 0; target =0
    scoville.sort()

    for n, x in enumerate(scoville):
        if(x>K):
            target =n
            break

    def check_K(times):
        if(scoville[0] >=K):
            return True
        if(len(scoville)==1):
            return True
        return False

    def sum_it(small,big):
        return small + big*2

    def put_it(this):
        i =0
        try:
            while(scoville[i]<this):
                i+=1
        except:
            scoville.insert(i, this)
        # print(scoville)

    def one_two():
        i =0; temp1 =scoville[0]; temp2=0
        while(True):
            if(scoville[i]>temp1):
                temp2 =scoville[i]
                break
            i+=1
        scoville.pop(i)
        scoville.pop(0)
        put_it(sum_it(temp1, temp2))

    while(True):
        one_two()
        answer+=1
        if(check_K(answer)):
            break

    if(len(scoville)==1):
        if(scoville[0]<K):
            return -1

    return answer


if __name__=='__main__':
    print('내 답 : ', solution([1, 2, 3, 9, 10, 12],7) )
    print('정답  : ', 2)
    print('-----------------------------')
    print('내 답 : ', solution([0,0,0,3],7) )
    print('정답  : ', 3)
