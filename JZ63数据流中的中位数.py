'''author: Shu YuTou Date:2020/8/10'''
class Solution:
    def Insert(self, num):
        # write code here
        midnumber = self.GetMedian(num)
        return midnumber

    def GetMedian(self,data):
        if len(data) % 2 == 0:  # 为偶数
            data.sort()
            a = data[len(data) // 2 - 1]
            b = data[len(data) // 2]
            return (a + b) // 2
        # if len(data) % 2 == 1:
        else:
            data.sort()
            midnum = data[(len(data) - 1) // 2]
            return midnum
if __name__ == '__main__':
    s =Solution()
    numbers =[5,2,3,4,1,6,7,0,8]
    numbers.sort()
    # print(a)
    print(numbers)
    print(s.Insert(numbers))