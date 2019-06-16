def solution(leng, max_w, t_w):
    if(len(t_w)==1):
        return leng+1
    time = 0
    k=len(t_w)
    arrive=0
    on_bridge=[]
    while(arrive<k):
        temp=[]
        # print('무게:',sum([x[0] for x in on_bridge])+t_w[0])
        if(len(t_w)>0):
            if(sum([x[0] for x in on_bridge])+t_w[0]<=max_w):
                on_bridge.append([t_w.pop(0),leng])
        # print('현재 다리 위:',on_bridge)
        # print('대기중 :',t_w)

        for n,truck in enumerate(on_bridge):
            truck[1]-=1
            if(truck[1]<1):
                temp.append(n)
        time+=1
        for remove in temp:
            on_bridge.pop(remove)
            arrive+=1
        # print('다리 위 :',on_bridge)
        # print('다리에 있는 트럭 :',on_bridge, '무게 :',sum(on_bridge))

    return time+1

if __name__=='__main__':
    print('내 답 :',solution(2, 10, [7,4,5,6]))
    print('답    :',8)
    # print('내 답 :',solution(100, 100, [10]))
    # print('답    :',101)
    print('내 답 :',solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
    print('답    :',110)
