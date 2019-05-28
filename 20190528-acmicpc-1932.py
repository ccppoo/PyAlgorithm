## problem source : https://www.acmicpc.net/problem/1932
## Unsolved : 2019 - 05 -28 (Tue)

## Olympiad > International Olympiad in Informatics > IOI 1994 problem 1
## number triangle
## 삼각형 크기 1~500, 정수 범위 0~9999


def main():
    import sys

    size_tri = int(sys.stdin.readline())
    pyramid =[]
    for _ in range(size_tri):
        pyramid.append([[n,int(x)] for n,x in enumerate(sys.stdin.readline().strip().split())])

    ## input 1, 1 2, 1 2 3
    '''
    pyramid = [ [[0, 1]],
                [[0, 1], [1, 2]],
                [[0, 1], [1, 2], [2, 3]]
    ]
    '''


    def same_values(index, values, depth,limit):
        '''중요한 점은 같은 값이 계속 나올 수 있다는 것이다, 예: 4만 있는 피라미드
        받는 값, 인덱스 실제값도 그냥 리스트로 받는게 안전 나중에 2의 n승까지 가능하니깐'''

        def strip_same(lists):
            temp =[]
            for x in range(len(lists)-1):
                if(lists[x]==lists[x+1]):
                    temp.append(lists[x])
            for x in temp:
                lists.remove(x)

        ln = len(index)
        index *=2; values *=2
        depth +=1
        for n, i in enumerate(index[:ln]):
            # 왼쪽 대각선
            values[n] += pyramid[depth][i][1]
            index[n] += 0
            # 오른쪽 대각선
            values[n+ln] += pyramid[depth][i+1][1]
            index[n+ln] +=1
            max_value =max(values)

        temp = [[i,v] for i,v in zip(index, values) if v==max_value]

        if(len(temp) == 1 or depth==limit):
            # print('type of temp[0]', type(temp[0]))
            return [temp[0]], depth
        strip_same(temp)
        return same_values(index,values,depth,limit)

    i=1

    curr =[x for x in pyramid[0]] # 구할 다음 층의 합 저장하는 리스트 (합이 같은 경우도 있으므로 리스트안에 리스트)
    # print('curr :', curr, type(curr))
    depth =0
    size_tri -=1
    while(depth<size_tri):
        depth+=1
        for x in curr:
            # 왼쪽 대각선 합(숫자)
            # print('x :',type(x), 'pyramid :',type(pyramid))
            a = x[1] + pyramid[depth][x[0]][1]
            a_index =  x[0]
            # 오른쪽 대각선
            b = x[1] + pyramid[depth][x[0]+1 ][1]
            b_index =  x[0] + 1
            if(a!=b):
                curr =[[a_index, a]] if a>b else [[b_index, b]]
                # print('curr :', curr, type(curr))
            elif(a==b and depth<size_tri):
                two_index=[a_index,b_index]
                two_values =[a,b]
                curr, depth = same_values(two_index, two_values, depth, size_tri)


    print(curr[0][1])

if __name__=='__main__':
    main()
#
