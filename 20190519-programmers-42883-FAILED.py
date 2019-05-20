## problem source : https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
## Unsolved : 2019 - 05 -19 (Sun) .. 05 -20(Mon) Thinking Thinking...
## it's not about programming, it's mathmatic sense

##  정확성 테스트 :

## 예외처리가 중요한...!!
## 알듯하면서 예외를 생각하지 못하는게 답답해 죽을 노릇

def solution(number, k):
    answer = ''
    num_list =[]
    length =0
    for n, x in enumerate(list(str(number) ) ):
        num_list.append([int(x), n])
        length =n

    # 숫자의 자리수가 작고, 제거할 숫자의 개수의 2배보다 작을 경우
    # 제일 작은 숫자부터 제거하면 된다.
    def mass_impact():
        temp_list =sorted(num_list)
        temp_list = temp_list[0:k]
        for x in temp_list:
            num_list.remove(x)
        temp=[]
        for x in num_list:
            temp.append(str(x[0]))
        answer =''.join(temp)
        return answer

    # 숫자의 자리수가 작고, 제거할 숫자의 개수의 2배보다 작을 경우
    # 제일 작은 숫자부터 제거하면 된다.
    def less_impact():

        def check_front(start, k_left):
            if(num_list[0] != 9):
                min_ = []
                tempp= []
                print('여기 중에서 :', num_list[1:k_left+1], end=' ')
                for x in (num_list[start:start+k_left+1]):
                    tempp.append([x[0], x[1]])
                num_list.remove(min(tempp))
                print('제거한거 :', min(tempp))
                k_left -=1
            return k_left

        start =0
        k_left = k
        # k번 만큼 제거
        for _ in range(k):
            if(k_left<1):
                break
            min_num = [999,0]   # [ number, index]
            print(num_list)

            for x in num_list[start:start +k_left]:
                # print('From :',start, 'To :', start+k_left)
                if(min_num[0]> x[0]):
                    min_num = x
            print(_,' 번째, 제거된 수: ', min_num[0])
            num_list.remove(min_num)

            k_left = check_front(start, k_left)
            if(min_num[1]<start+k_left):
                k_left -=1
            else:
                print('FLAG')
                start +=1
                k_left -=1
            # 417725 같은 경우에
            # 1이 제거되고 나서, 인덱스를 늘릴 수 없음
        temp=[]
        for x in num_list:
            temp.append(str(x[0]))

        answer =''.join(temp)
        return answer

    if(k*2 >= length):
        return mass_impact()
    else:
        return less_impact()


if __name__=='__main__':

    # print('솔루션 ! :', solution(1924,2))
    # print('answer : ' ,94, end='\n\n')
    print('솔루션 :', solution(1231234, 3))
    print('answer : ', 3234, end='\n\n')
    print('솔루션 :', solution(4177252841,4))
    print('answer :',775841, end='\n\n')

    print('솔루션 :', solution(11111111111122299,12))
