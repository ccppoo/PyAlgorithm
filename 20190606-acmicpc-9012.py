from sys import stdin

n= int(stdin.readline())

def count():
    temp = list(stdin.readline())
    temp.pop()
    if (len(temp)%2==1):
        print('NO')
        return 
    if(temp.count('(')!=temp.count(')')):
        print('NO')
        return
    else:
        n=0
        for x in temp:
            if(x=='('):
                n+=1
            elif(x==')'):
                n-=1
            if(n<0):
                print('NO')
                return
    print('YES')

for _ in range(n):
    count()




#
