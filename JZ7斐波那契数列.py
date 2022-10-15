#author: Shu YuTou Date:2020-7-16
# print("斐波那契数列")
#循环的方法
class Solution:
	def Fibonacci(self,n):
		'''方法一：利用递归算法'''
		if n == 0:
			return 0
		if n==1:
			return 1
		else:
			num = self.Fibonacci(n-1)+self.Fibonacci(n-2)
		return num
		'''方法二：非递归算法'''
		if n == 0:
			return 0
		# n=1,num=1
		if n == 1:
			return 1
		# if n>1   f(n)=f(n-1)+f(n-2)
		if n > 1:
			a = 0
			b = 1
			sum=0
			for i in range(2, n+1):
				sum = a + b
				a = b
				b = sum
			return sum
	
if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(4))
    
