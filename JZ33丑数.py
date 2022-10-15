#author: Shu YuTou Date:2020-7-20
#穷举
#思路：一个丑数都是由另一个丑数乘以2或3或5得到，且要按从小到大排列，选出由上一组丑数获得的新的丑数的最小值排在列表的后面，
# 得出新的丑数后，通过更新列表的索引数来获得上一轮刚刚获得的丑数，用来获得下一轮的丑数，即将刚刚获得丑数最为下一轮丑数的因子。
class Solution:
    def GetUglyNumber_Solution(self, n):
        # write code here
        if(n<=0):
            return 0
        uglylist=[1]
        indexTwo=0
        indexThree=0
        indexFive=0
        for i in range(0,n-1):
            newugly=min(uglylist[indexTwo]*2,uglylist[indexThree]*3,uglylist[indexFive]*5)
            uglylist.append(newugly)
            if (newugly % 2 == 0):
                indexTwo += 1
            if (newugly % 3 == 0):
                indexThree += 1
            if (newugly % 5 == 0):
                indexFive += 1
        return uglylist[n-1]#取出列表的最后一个元素
if __name__ == '__main__':
    s=Solution()
    print(s.GetUglyNumber_Solution(2))
    
