'''author: Shu YuTou Date:2020-7-29'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        #方法一：思路：遇到不相同的数字就相互抵消掉，那么最终剩下的数字就可能是出现次数大于一半的数字,时间复杂度O(n),空间复杂度O(1)
        # last = 0
        # lastCount = 0
        # for num in numbers:
        #     if lastCount == 0:
        #         last = num
        #         lastCount =1
        # else:
        #     if num == last:
        #         lastCount += 1
        #     else:
        #         lastCount -= 1
        # if lastCount == 0:
        #     return 0
        # else:
        #     lastCount = 0
        #     for num in numbers:
        #         if num == last:
        #             lastCount += 1
        #     if lastCount > (len(numbers)/2):
        #         return last
        # return 0
        #方法二：时间复杂度O(n),空间复杂度O(n)
        numsCount = {} #利用字典将num作为key,num出现的次数作为key 的 value
        numlen = len(numbers)
        for num in numbers:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
            if numsCount[num] > (numlen//2): #该判断条件在循环体内部
                return num
        return 0


if __name__ == '__main__':
    s = Solution()
    numbers=[2,2,1,3,4,5,2,2,2,]
    num = s.MoreThanHalfNum_Solution(numbers)
    print(num)