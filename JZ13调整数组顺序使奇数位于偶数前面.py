# #author: Shu YuTou Date:2020-7-20
class Solution():
	def reOrderArray(self,array):
		ret=[]
		odd=[]#奇数
		even=[]#偶数
	
		for i in range(0,len(array)):
			if array[i]%2==0:
				even.append(array[i])
			elif array[i]%2!=0:
				odd.append(array[i])
		ret=odd+even
		return ret
		
if __name__ == '__main__':
    s= Solution()
    print(s.reOrderArray([1,2,5,25]))