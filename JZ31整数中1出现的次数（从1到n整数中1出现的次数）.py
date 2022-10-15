'''author: Shu YuTou Date:2020-7-29'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 循环的出口
        # highValue = 1
        # midValue = 1
        # lowValue = 1
        # preceise = 1
        # count = 0
        # sumNum = 0
        # while highValue != 0:
        #     lowValue = n % preceise
        #     midValue = (n // preceise) % 10
        #     highValue = n // (preceise * 10)
        #     preceise = preceise * 10
        #
        #     if midValue == 0:
        #         num = (highValue - 1 + 1) * pow(10, count)
        #
        #     elif midValue > 1:
        #         num = (highValue + 1) * pow(10, count)
        #
        #     else:
        #         num = (highValue) * pow(10, count) + lowValue + 1
        #     sumNum += num
        #     count += 1
        # return sumNum
        
        # res=0
        # tmp=n
        # base=1
        # while tmp:
        #     last=tmp%10
        #     tmp=tmp//10
        #     res+=tmp*base
        #     if last==1:
        #         res+=n%base+1
        #     elif last>1:
        #         res+=base
        #     base*=10
        # return res
        sum = 0
        for i in range(1,n+1):
            x =i
            while x!=0:     #将数字逐位取出
                if x%10==1:
                    sum+=1
                    x = x // 10
                if x%10!=1:
                    x= x //10
        return sum
if __name__ == '__main__':
    s = Solution()
    cou = s.NumberOf1Between1AndN_Solution(231)
    print(cou)