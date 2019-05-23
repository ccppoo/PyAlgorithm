## problem source : https://programmers.co.kr/learn/courses/30/lessons/42586
## Unsolved : 2019 - 05 -23 (Thur)

## level 2 problem in programmers
## took about 20 mins

## progress, speeds 배열 크기 최대 100개, 자연수
def solution(progresses, speeds):
    print('시작 일 :', progresses)
    print('   속도 :', speeds)
    answer = []

    def work_work():
        for i in range(0,len(progresses)):
            progresses[i] = progresses[i] +speeds[i]
        # print('일 했습니다 :',progresses)

    def check_once():
        for i in range(len(progresses)):
            t=0
            if(progresses[i] >=100):
                t =check_twice(i)
                if(t):
                    answer.append(t)
                    for _ in range(t):
                        progresses.pop(0)
                        speeds.pop(0)
                    print('\n남은 일  :',progresses)
                    print('처리 속도 : ', speeds)
                    return

    def check_twice(index):
        work_done =0
        # 맨앞에 있는 작업 확인
        for ck in progresses[:index]:
            if(ck<100):
                return False
        # 자신 뒤에 있는 작업확인(순서대로!!)
        for i in range(index, len(progresses)):
            if(progresses[i] >=100):
                work_done +=1
            else:
                return work_done
        return work_done

    while(len(progresses) != 0):
        work_work()
        check_once()

    return answer

if __name__=='__main__':
    # print('내 답: ',solution([93,30,55],[1,30,5]))
    # print('답   : [2,1]')
    # print('-------------------------------------------------------')
    print('\n내 답: ',solution( [40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))
    print('답   : [1,2,3]')
    print('-------------------------------------------------------')
    print('\n내 답: ',solution( [93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7]))
    print('답   : [2,4]')
