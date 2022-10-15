'''author: Shu YuTou Date:2020-8-3'''
class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		a=[]
		for n in array:
			if n in a:
				a.remove(n)
			else:
				a.append(n)
		return a


if __name__ == '__main__':
	array = [1,2,1,4,3,4,5,5]
	s = Solution()
	print(s.FindNumsAppearOnce(array))
