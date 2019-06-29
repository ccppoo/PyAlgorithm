def solution(T, R):
    i=0
    dic_live ={}
    dic_dead={}
    while(T[0][i].isalpha()):
        i+=1
    n=i
    for k, word in enumerate(T):
        i=n
        try:
            while(word[i].isnumeric()):
                i+=1
        except:
            pass
            # print(i-1, word[i-1])
        # i-1 까지 숫자
        try:
            dic_dead[int(word[n:i])]
        except:
            if(R[k]=="OK"):
                try:
                    dic_live[int(word[n:i])]
                except:
                    dic_live.update({int(word[n:i]):0})
            else:
                dic_live.pop(int(word[n:i]),None)
                dic_dead.update({int(word[n:i]):0})
    return int(len(dic_live.keys())/(len(dic_live.keys())+len(dic_dead.keys()))*100)


if __name__=='__main__':
    T=["test1a","test2","test1b","test1c","test3"]
    R=["Wrong answer", "OK","Runtime error","OK","Time limit exceeded"]
    print(solution(T,R), 'Answer should be :',33)
