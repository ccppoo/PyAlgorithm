## problem source : https://programmers.co.kr/learn/courses/30/lessons/49993
## Unsolved : 2019 - 06 -02 (Sun)

##

def solution(skill, skill_trees):
    answer = 0
    li_sk = [k for k in skill]
    sk_tr = [ [k for k in x] for x in skill_trees]
    for x in sk_tr:
        temp=[]
        for k in x:
            if(k not in li_sk):
                temp.append(k)
        for t in temp:
            x.remove(t)
        if(skill.startswith(''.join(x))):
            print(x)
            answer+=1
    return answer

if __name__=='__main__':
    print('내 답:',solution('CBD',['BACDE', 'CBADF', 'AECB', 'BDA', 'CAD','CB']))
    print('\n답: 3')
