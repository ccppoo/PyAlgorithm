## problem source : https://programmers.co.kr/learn/courses/30/lessons/12900
## Unsolved : 2019 - 06 -03 (Mon)

##

def solution(n):
    answer = 1
    temp =1

    for i in range(n):
        answer, temp = temp, answer+temp
    return answer%1000000007

if __name__=='__main__':
    print(solution(7))
