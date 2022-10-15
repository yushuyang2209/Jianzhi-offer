'''author: Shu YuTou Date:2020-7-29'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        s=[]
        s.append(num1)
        s.append(num2)
        return sum(s)
if __name__ == '__main__':
    s =  Solution()
    print(s.Add(1,2))