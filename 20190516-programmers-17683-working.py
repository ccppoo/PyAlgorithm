## problem source : https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3
## Unsolved : 2019 - 05 -16 (Thur) ~ ...

##  정확성 테스트 :
##  효율성 테스트 :

# 한 가지의 노래가 여러번 재생될 수 있고, 노래1과 노래2가 연속으로 재생되는 경우,
# (노래1 끝부분 + 노래2 초반) 구성으로 문제의 함정을 심을 것이다.
# 그래서 노래가 일치하는 구간이 있더라도 ... 두 노래가 연속 재생되어서 발생한 문제
import re

def solution(humming, musicinfos):
    length = len(musicinfos)
    time_stamp = [] # time_stamp[n][0], [1] : 분 단위의 노래 시작시간, 종료시간
                    # time_stamp[n][2] : 재생된 시간 ; 안 만들어도 됨
    title =[]   # title[n] : n-1 번째 곡의 제목
    melody = [] # melody[n][0] : n-1번째 곡의 전체 멜로디, melody[n][1] : n-1번째 곡의 길이

    # 연달아 다른 곡이 재생되는 경우, 나중에 검증 후 확인 할 것(추가로)
    sequence =[]    # 노래 재생이 연달아 되는 경우 확인

    hum_len = 0

    def sharp_go_away( mel):
        temp =list(mel)
        temp_list =[]
        for n, melody in enumerate(temp):
            if temp =='#':
                temp_list.pop()
                temp_list.append(temp[n-1].lower())
            else:
                temp_list.append(temp[n])
        return ''.join(temp_list)

    def preprocessing():
        # 주어진 정보 리스트를 재생된 시간, 제목, 멜로디로 구분
        for n, x in enumerate(musicinfos):
            time_stamp.append(x.split(',')[0:2])
            title.append(x.split(',')[2])
            melody.append([ x.split(',')[3] ])

        # 시간은 문자열에서 분(min)단위의 int로 변환, 노래는 인덱스로 구분됨
        # melody옆에 재생된 시간(min) 저장, 나중에 반복 재생된 노래의 경우 그 시간만큼 대조 배열 생성
        for n, t2 in enumerate(time_stamp):
            for m, t in enumerate(t2):
                time_stamp[n][m] = int(t.split(':')[0])*60 + int(t.split(':')[1])

            time_stamp[n].append(time_stamp[n][1] - time_stamp[n][0])   #곡의 재생된 시간 melody[n][1]
            melody[n].appned(len(sharp_go_away(melody[n][0]))) #곡의 길이 melody[n][2]

        # 두 곡이 연달아 재생되는 경우
        for x in range(0, length-1):
            if(time_stamp[x][1] == time_stamp[x+1][0]):
                sequence.append(x)

    preprocessing()

    humming =sharp_go_away(humming)

    # 1차 : 노래 곡마다 단순 대조
    count = 0
    for n in range(length):
        # 재생 시간이 노래 원곡보다 길 수도 있고, 짧을 수도 있다.
        for m in range(0, abs(melody[n][1] - time_stamp[n][2])):
            if(melody[n][0][m % melody[n][1]] != humming[m]):
                break
            else:
                count +=1
        if(count == len(humming)):
            return title[n]

    # 2차 : 연속 재생된 노래 확인

    answer = '(None)'
    return answer


if __name__ =='__main__':
    # 시작, 끝, 제목, 음의 구성
    sample1_1 = 'ABCDEFG'
    sample1_2 = ["12:00,12:14,HELLO,CDEFGAB", '13:00,13:05,WORLD,ABCDEF']
    answer_1 = 'HELLO'

    sample2_1 = 'CC#BCC#BCC#BCC#B'
    sample2_2 = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']
    answer_2 = 'FOO'

    sample3_1 = 'ABC'
    sample3_2 = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']
    answer_3 = 'WORLD'
    solution(sample1_1, sample1_2)
    print('answer 1 : ', answer_1)
    solution(sample2_1, sample2_2)
    print('answer 2 : ', answer_2)
    solution(sample3_1, sample3_2)
    print('answer 3 : ', answer_3)
