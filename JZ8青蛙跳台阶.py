#author: Shu YuTou Date:2020-7-19
class Solution:
    def jumpFloor(self, number):
        # write code here
        a=0
        b=1
        m=0
        for i in range(1,number+1):
            m=a+b
            a=b
            b=m
        return m
if __name__ == '__main__':
    s=Solution()
    print(s.jumpFloor(5))