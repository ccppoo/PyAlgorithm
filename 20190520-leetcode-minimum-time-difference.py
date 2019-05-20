## code source : https://leetcode.com/problems/minimum-time-difference/description/
## 2019-05-21 (Mon) ...
## solution is too slow and easy one

# class Solution:
#     def findMinDifference(self, timePoints: List[str]) -> int:

from copy import deepcopy
def Solution(List):
    diff =0
    mins =[]
    for x in List:
        temp = x.split(':')
        mins.append(int(temp[0])*60+int(temp[1]))
    length = len(mins)

    mins.sort()
    mins_re = deepcopy(mins)
    mins_re.reverse()
    for i in range(0,length):
        mins_re[i] = mins[i] -mins_re[i] + 1440

    for i in range(0, length-1):
        mins[i]= mins[i+1]-mins[i]


    return min(mins) if min(mins) <min(mins_re) else min(mins_re)

if __name__=='__main__':
    ## 여기에 input되는 리스트에 많이 들어가있을 수 있음

    print(Solution(["12:12", '00:13']))
    print(Solution(["00:00", '23:59']))

'''
Input: ["23:59","00:00"]
Output: 1'''
