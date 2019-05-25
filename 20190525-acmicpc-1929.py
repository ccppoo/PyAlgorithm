## problem source : https://www.acmicpc.net/problem/4673
## Unsolved : 2019 - 05 -25 (Sat)

## getting self nuber
''' 파이썬의 문자열은 불변값이기 때문에
    숫자를 문자열로 만든 후 인덱싱하는 작업은
    매번 복사후 저장하는 작업이라시간을 많이 차지한다
    for문을 통해 각 자리수에 로그를 취해서 self number를 구한다
    '''
from math import log10 as lg
from math import pow

def get_selfnum(N):

    self_num_list=[x for x in range(1,N+1)]

    def check_n_selfnum(num):
        temp=[num]
        k=9
        while(k>1):
            k =int(lg(num+0.1))
            t   =int(num//pow(10, k ))
            num =int(num%pow(10, k))
            temp.append(t)
            # print('k:', k ,' num: ',num)
        temp.append(num%10)
        # print('temp : ', temp, 'remove : ',sum(temp))
        try:
            self_num_list.remove(sum(temp))
        except:
            pass

    i=0
    for x in range(1,N+1):
        # print('length of num_list : ', len(num_list), 'ck :', ck)
        check_n_selfnum(x)
    return self_num_list

if __name__=='__main__':
    rep = get_selfnum(64)
    print(rep)
