#author: Shu YuTou Date:2020-7-21
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
class Solution:
	# array 二维列表
	def Find(self, target, array):
		# write code here
		#1,2,3,4
		#3,4,5,6
		#4,6,8,9
		#6,7,9,11
		if array==[] or  target<array[0][0] or target>array[len(array)-1][len(array[0])-1]:
			return None
		
		for i in range(0,len(array)):#行数
			
			for j in range(0,len(array[0])):#列数
				if array[i][j]==target:
					return True
		return None
		# for i in range(0,len(array)):
		
		
if __name__ == '__main__':
    s=Solution()
    a=[[1,2,3],[2,4,5],[5,7,9],[8,9,10]]
    print(s.Find(10,a))