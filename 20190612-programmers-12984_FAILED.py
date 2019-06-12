## problem source : https://programmers.co.kr/learn/courses/30/lessons/12984
## Unsolved : 2019 - 06 - 12 (Wend)

def solution(land, P, Q):
    # for land 0<= N <= billion (10^8)
    # cost P(add block), Q(remove block) 1~100
    if(len(land)==1):
        return 0
        '''
        cost = sigma(abs(ave-x)*Q for x in land if(ave-x)> 0 else abs(ave-x)*P)
        평균과 떨어진 거리 i_0_0, i_0_1, ... , i_n-1_n-1
        첫 지형의 평균블럭 수를 기준으로, 높이를 낮출 것인지 높일것인지 스캔
        --> n*n개의 1차 방정식 중에서 최소를 구하라, 단 기울기는 두가지 ( -P, -Q)
        cost_i  = x-y(기준 높이)<0 : (x-y)*Q
        = x-y(기준 높이)>0 : (x-y)*P

        기준 높이를 기준으로 길이가 n*n 인 정수 리스트 생성(최악 300*300=90000)
        기준높이를 중심으로 높이를 교차로 +-1 을하면서 비용이 증가하는지, 감소하는지 계속 검사
        이 검사를 2진 탐색으로 최대 높이가 10억 까지니깐 최악의 경우 24번으로 검사를 할 수 있음 (2^24~= 16억)
        n^2*k -> O(n^2)
        기울기가 2가지인 n개의 1차함수 = 1차함수 이므로

        2차 함수, 지역 최소 값 찾기
        '''
    cost=0
    heights =[x for row in land for x in row]
    max_height =max(heights)
    min_height=min(heights)
    search_len=max(heights) -min(heights)   # 높이 구간
    ave = sum(heights)//(len(land)*len(land))
    li=[]
    mask =[x-ave for row in land for x in row]

    def cost(list_of_heights, ch=None):
        temp_sum=0
        if(ch!=None):
            ttmp =[ch-x for x in list_of_heights]
            # print(ttmp, end=' ')
            for x in ttmp:
                if(x>0):
                    temp_sum+=(x)*P
                elif(x<0):
                    temp_sum+=(abs(x))*Q
            return temp_sum
        for x in list_of_heights:
            if(x>0):
                temp_sum+=x*P
            elif(x<0):
                temp_sum+=abs(x)*Q
        return temp_sum

    def increase(list, i=1):
        return [x+i for x in list]
    def decrease(list, i=1):
        return [x-i for x in list]
    def price(list):
        cost=0
        for x in list:
            if(x>0):
                cost+=x*Q
            elif(x<0):
                cost-=x*P
        return cost

    def go_right(bottom, top,i=0):
        temp_li=[]
        if((top-bottom)//10>2):
            for h in range(0,top-bottom,(top-bottom)//10):
                temp_li.append([price(increase(mask, i+h)), i+h])
        else:
            for h in range(0,(top-bottom),1):
                temp_li.append([price(increase(mask, h)),  i+h])
            return min(temp_li)[0]

        temp_li.sort()
        if(temp_li[0][1]>temp_li[1][1]):
            return go_right(top+temp_li[1][1],top+temp_li[0][1] ,temp_li[1][1])
        if(temp_li[0][1]<temp_li[1][1]):
            return go_right(top+temp_li[0][1],top+temp_li[1][1] ,temp_li[0][1])

    def go_left(bottom, top,i=0):
        temp_li=[]
        if((top-bottom)//10>2):
            for h in range(0,top-bottom,(top-bottom)//10):
                temp_li.append([price(decrease(mask, i+h)),  i+h])
        else:
            for h in range(-(top-bottom),0,1):
                temp_li.append([price(decrease(mask, h)),  i+h])
            return min(temp_li)[0]

        temp_li.sort()
        if(temp_li[1][1]>temp_li[0][1]):
            return go_left(bottom+temp_li[0][1],bottom+temp_li[1][1] ,temp_li[1][1])
        if(temp_li[1][1]<temp_li[0][1]):
            return go_left(bottom+temp_li[1][1],bottom+temp_li[0][1] ,temp_li[0][1])
    # 근이 없고, 아래로 볼록한 2차 함수 꼴에서 오르는 경우(오른쪽으로 탐색)

    if(price(mask)<price(increase(mask)) and price(mask)<price(decrease(mask))):
        return price(mask)
    if(price(mask)>price(increase(mask))):
        return go_right(min_height, max_height)
    # 근이 없고, 아래로 볼록한 2차 함수 꼴에서 오르는 경우(왼쪽으로 탐색)
    elif(price(mask)<price(increase(mask))):
        return go_left(min_height, max_height)

if __name__=='__main__':
    print(solution([[4,4,3],[3,2,2],[2,1,0]], 5,3))
    print('\n답 : 33')
    import random
    li=[]
    for x in range(300):
        li.append([random.randint(1, 1000000000) for x in range(300)])
    # for x in range(300):
    #     li.append([0 for x in range(300)])
    print(solution(li, random.randint(1,100), random.randint(1,100)))



    #
