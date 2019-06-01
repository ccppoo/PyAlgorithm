## problem source : https://www.acmicpc.net/problem/1780 ->precise one
## Unsolved : 2019 - 06 -01 (Sat)

## 주어진 사각형 가로,세로 2이상의 모든 사각형 찾기 문제로 풀어버렸다...

'''
꼭지점은 동일 숫자 + 내부에도 같은 숫자 , 한변의 길이 최대 3^7 = 6561
검색 순서 : 상단 왼쪽 꼭지점 -> 하단 왼쪽 꼭지점 (높이 구함)
            -> 높이만큼 옆으로 스캔 -> 만족하는 횟수 == 사각형의 개수'''


import sys
n = int(sys.stdin.readline().strip())
matrix =[]
for _ in range(n):
    matrix.append(sys.stdin.readline().split())
matrix =[ [int(k) for k in x] for x in matrix]

square_0=0
square_1=0
square_2=0

def height_search(top_left,y, x):
    i =y+1; j = x
    temp=[]
    while(i<n):
        if(matrix[i][j] == top_left):
            temp.append([top_left,y, i, x])
        i+=1
    print(temp)
    return temp

def scan2right(height, type):
    sqr =0
    for info in height:
        flag =True
        xxx = info[3]
        ## 그냥 xxx 인 경우 : 가로 길이 1도 가능
        for x in range(xxx+1, n):
            ## 그냥 info[2]인 경우 : 세로길이 1도 가능
            for y in range(info[1], info[2]+1):
                if(info[0] != matrix[y][x]):
                    flag=False
                    break
            if(flag):
                sqr +=1
            print('카운트 sqr :',sqr)
    print()
    return type, sqr

for y in range(n):
    for x in range(n):
        li = height_search(matrix[y][x], y, x)
        if(len(li)):
            type, cnt =scan2right(li, matrix[y][x])
            if(type ==-1):
                square_0+=cnt
            elif(type ==0):
                square_1+=cnt
            elif(type ==1):
                square_2+=cnt

print('-1 사각형 :',square_0)
print(' 0 사각형 :',square_1)
print(' 1 사각형 :',square_2)










#
