## problem source : https://www.acmicpc.net/problem/10866
## Unsolved : 2019 - 05 -27 (Mon)

## making deque
'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys

class dequeee:
    def __init__(self):
        self.li_size=0
        self.deque_list = []

    def push_front(self, X):
        self.deque_list.insert(0, X)
        self.li_size +=1

    def push_back(self, X):
        self.deque_list.insert(self.li_size, X)
        self.li_size +=1

    def pop_front(self):
        if(self.li_size):
            print(self.deque_list.pop(0))
            self.li_size -=1
        else:
            print(-1)

    def pop_back(self):
        if(self.li_size):
            print(self.deque_list.pop(self.li_size-1))
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
            print(self.deque_list[0])
        else:
            print(-1)

    def back(self):
        if(self.li_size):
            print(self.deque_list[self.li_size-1])
        else:
            print(-1)
if __name__=='__main__':
    new_deque =dequeee()
    times =int(sys.stdin.readline())
    sys.stdin.flush()
    cmd_list ={ 'push_front':new_deque.push_front,
                'push_back':new_deque.push_back,
                'pop_front':new_deque.pop_front,
                'pop_back':new_deque.pop_back,
                'size':new_deque.size,
                'empty':new_deque.empty,
                'front':new_deque.front,
                'back':new_deque.back
    }
    for _ in range(times):
        str =sys.stdin.readline()
        temp =str.split()
        if(temp[0].startswith('push')):
            if(temp[0].endswith('front')):
                new_deque.push_front(int(temp[1]))
            elif(temp[0].endswith('back')):
                new_deque.push_back(int(temp[1]))
        else:
            if temp[0] in cmd_list:
                cmd_list[temp[0]]()

        sys.stdin.flush()
