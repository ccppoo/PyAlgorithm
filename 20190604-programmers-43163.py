## problem source : https://programmers.co.kr/learn/courses/30/lessons/43163
## Unsolved : 2019 - 06 -03 (Mon)

##
from copy import deepcopy

def solution(begin, target, words):
    if(target not in words):
        return 0

    answer = 0
    # 목표 단어를 마지막 인덱스로 옮김
    words.append(words.pop(words.index(target)))
    words  = [[k for k in x] for x in words]
    begin  = [x for x in begin]
    # 시작 단어를 맨 첫 인덱스오 옮김
    words.insert(0,begin)
    target = [x for x in target]
    matrix=[]

    def get_mask():
        for n,wds in enumerate(words):
            temp=[]
            for m,wd in enumerate(words):
                cnt=0
                for w, x in zip(wds, wd):
                    if(w!=x):
                        cnt+=1
                    if(cnt>1):
                        break
                temp.append(1 if cnt==1 else 0)
            matrix.append(temp)

    def not_same(a,b):
        for z,x in zip(a,b):
            if(z!=x):
                return True
        return False

    # 2차원 배열 만든다 -> 한글자만 바뀌면 바꿀수 있는 단어 1 아니면 0
    # 이것은 한붓그리기(섬과 다리 )랑 같은 개념이다 (최단거리, 중복해서 건너기 X)
    # 처음에 만들것 : begin(1) + words(n) = n+1, (n+1)*(n+1) 2차원 배열 만듦
    get_mask()

    # 시작은 0 0에서 갈수 있는건 matrix[0][?](또는 matrix[?][0])에 있다
    # 깊이 우선 탐색으로 하자
    possible_route =[]
    start=0
    end=len(words)-1
    temp =[[0]] # 지금까지 온 길, possible_route에 append 할 것
    loc=0
    # 이 함수는 재귀고, 한번에 한 번씩 이동

    def find_route(loc, temp):
        global count
        count +=1
        # 가능한 길 탐색
        for i in temp:
            tp =[matrix[i[-1]][x] for x in range(len(words))]
            # 길이 하나라도 있는 경우
            if(any(tp)):
                pass
                # print('가능한 경로 :',tp)
            else:
                # print('no route after this :',i )
                temp.remove(i)
                continue
            if(tp[-1]==1):
                # print('마지막 움직임 :', tp)
                length = [len(x) for x in temp]
                length.sort()
                return length[-1]

        for k in range(len(temp)):
            flag=False
            for x in range(len(words)):
                # 갈 수 있는 길 and 이미 왔던 길 x
                if(matrix[loc][x]==1 and x not in temp[k]):
                    if(flag):
                        temp.append(deepcopy(temp[k]))
                        temp[-1].append(x)
                    flag=True
                    temp[k].append(x)

        for rt in temp:
            if(rt[-1]==len(words)-1):
                # return len(rt), temp
                return rt


        return find_route(temp[-1][-1], temp)

    return find_route(loc, temp)



if __name__=='__main__':
    print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
    # print('답 :', 4)
    # print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log']))
    # print('답 :', 0)
