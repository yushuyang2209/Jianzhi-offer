'''author: Shu YuTou Date:2020-7-23'''
'''题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
思路：设置两个栈，一个为原始栈，另一个存储比较前后值大小后的栈minvalue，在push时，若后值<=前值，则添加进来，否则仍然保留前值，
minvalue最后的那个值即为最小值，此外这样也可以保证两个栈的长度一致。所以在pop操作时直接弹出即可。'''
class Solution:
	#定义一个栈
	def __init__(self):
		self.stack=[]
		self.minvalue=[]
	def push(self, node):   #压入
		# write code here
		self.stack.append(node)
		if self.minvalue!=[]:
			if self.minvalue[-1] > node:
				return self.minvalue.append(node)
			else:
				self.minvalue.append(self.minvalue[-1])
		else:
			return self.minvalue.append(node)
	def pop(self):  #弹出栈顶并删除
		if self.stack==[]:
			return None
		self.minvalue.pop()
		return  self.stack.pop()
		# write code here
	def top(self):  #返回栈顶值
		if self.stack==[]:
			return None
		return self.stack[-1]
		# return self.stack[-1]
		# write code here
	def min(self):
		if self.minvalue==[]:
			return None
		return self.minvalue[-1]
if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(4)
    # s.push(6)
    print(s.min())