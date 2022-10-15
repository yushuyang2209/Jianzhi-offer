#author: Shu YuTou Date:2020-7-21
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        
        '''（贪心算法）
    若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列
        '''
        if array == []:
	        return 0
        if len(array) == 1:
	        return array[0]
        '''if len(array)<=0:
			return []'''
        temp_sum = 0
        list_sum = []
        for i in array:
	        temp_sum = temp_sum + i
	        list_sum.append(temp_sum)
	        if temp_sum > 0:
		        continue
	        else:
		        temp_sum = 0
        return max(list_sum)
    '''或者下面的方法动态规划，若前面的元素大于0，则将其加到当前元素上
    '''
    '''res =max(array)
        temp = 0
        for i in array:
            temp = max(i,temp+i)
            res = max(res,temp)
        return res
        '''
    
    
if __name__ == '__main__':
    a=[-5,-8,9,10,-12]
    s= Solution()
    print(s.FindGreatestSumOfSubArray(a))
