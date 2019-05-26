## problem source : https://www.acmicpc.net/problem/10845
## Unsolved : 2019 - 05 -26 (Sun)

## making quuue
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞(가장 오래된)에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

처음에 주어지는 숫자는 명령의 수
'''
import sys

class quuue:
    # self.quuue_list =[]
    # self.size=0

    def __init__(self):
        self.li_size=0
        self.quuue_list = []

    def push(self, X):
        self.quuue_list.insert(0, X)
        self.li_size +=1

    def pop(self):
        if(self.li_size):
            print(self.quuue_list.pop(-1))
            self.li_size -=1
        else:
            print(-1)

    def size(self):
        print(self.li_size)

    def empty(self):
        if(self.li_size):
            print(0)
        else:
            print(1)

    def front(self):
        if(self.li_size):
            print(self.quuue_list[-1])
        else:
            print(-1)

    def back(self):
        if(self.li_size):
            print(self.quuue_list[0])
        else:
            print(-1)

if __name__=='__main__':
    new_que =quuue()
    times =int(sys.stdin.readline())
    sys.stdin.flush()
    cmd_list ={'pop':new_que.pop, 'size':new_que.size, 'empty':new_que.empty, 'front':new_que.front, 'back':new_que.back }
    for _ in range(times):
        str =sys.stdin.readline()
        temp =str.split()
        if('push' ==temp[0]):
            new_que.push(int(temp[1]))
        else:
            if temp[0] in cmd_list:
                cmd_list[temp[0]]()
        sys.stdin.flush()




#
