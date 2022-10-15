'''author: Shu YuTou Date:2020-7-22'''
'''题目：旋转数组的最小数字

'''
class Solution:
	def minNumberInRotateArray(self, rotateArray):
		'''直接找最小值
		if rotateArray==[]:
			return 0
		return min(rotateArray)
	    '''
		'''采用二分法
		思路：1.最小值一定比前面的数小；2.二分法:找left与right的方法，当中间值比right小时，right-1；当中间值比left大时，left+1。
		'''
		if rotateArray == []:
			return 0
		left = 0
		right = len(rotateArray) - 1
		min = 0
		while left <= right:
			mid = (left + right) // 2
			if rotateArray[mid] <= rotateArray[right]:
				min = rotateArray[mid]
				right = right - 1
			else:
				min = rotateArray[mid]
				left = left + 1
		return min
if __name__ == '__main__':
    s=Solution()
    print(s.minNumberInRotateArray([3,4,5,1,2]))