'''author: Shu YuTou Date:2020-7-29'''


class Solution:
	def NumberOf1(self, n):
		# write code here
		# 补码：正数不变，负数是它的正数的反码+1
		# -2 补码：2的二进制1 00000000....010，1 11111111.....101+1
		# -2 的补码就是 1 11111111.....110
		# n & 0xFFFFFFFF
		# 正数：11110010
		
		#方法一：先将n和32位全为1进行与运算
		# n = 0xFFFFFFFF & n
		# count = 0
		# for c in bin(n):    #bin()函数返回的是：将 n 转化为二进制的字符串。
		# 	if c == "1":
		# 		count += 1
		# return count
		
		
		#方法二：在计算机中，负数的二进制的表示形式就是补码表示的。
		cou=0
		for i in range(0,32):
			if (n >> i) & 1 == 1:#将 n 往右移，如 0001011 >> 为 000101
				cou += 1
		return cou
	
	
if __name__ == '__main__':
    s=  Solution()
    print(s.NumberOf1(5))