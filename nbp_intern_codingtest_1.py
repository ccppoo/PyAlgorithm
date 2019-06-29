def solution(A):
    cas=1
    flag=False
    i=0
    curr=A[0]
    # 처음에 상승, 하강 패턴 모르니깐 선빵
    while(curr==A[i]):
        curr=A[i]
        i+=1
        if(i==len(A)):
            return cas
        # 하강
        if(curr>A[i]):
            i-=1
            curr=A[i]
            tag=0
            break
        elif(curr<A[i]):
            i-=1
            curr=A[i]
            tag=1
            break
    while(i<len(A)):
        # 상승
        if(tag%2):
            print('상승')
            while(curr<=A[i]):
                curr=A[i]
                i+=1
                if(i==len(A)):
                    print('end :',i)
                    return cas+1
            cas+=1
            print('added ',i)
            tag+=1
        # 하강
        else:
            print('하강')
            while(curr>=A[i]):
                curr=A[i]
                i+=1
                if(i==len(A)):
                    print('end :',i)
                    return cas+1
            cas+=1
            print('added ',i)
            tag+=1

if __name__=='__main__':
    A =[2,2,3,4,3,3,2,2,1,1,2,2]
    print(solution(A), '-- Answer should be :', 4)
    A =[4,3,3,2,2,1,1,2,2]
    print(solution(A), '-- Answer should be :', 3)
    A=[3,3,3,3,3]
    print(solution(A), '-- Answer should be :', 1)
