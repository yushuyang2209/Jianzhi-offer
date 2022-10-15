#author: Shu YuTou Date:2020-7-20
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if (numbers[i]==numbers[j]):
                    duplication.append(numbers[i])
                    print(duplication[-1])
                    return True
        return False
if __name__ == '__main__':
    s=Solution()
    a=[0,3,4,5,2,3]
    b=[0]
    print(s.duplicate(a,b))
    