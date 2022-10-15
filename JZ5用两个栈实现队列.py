#author: Shu YuTou Date:2020-7-22
# -*- coding:utf-8 -*-
'''题目：用两个栈来实现一个队列，完成队列的Push和Pop操作
知识点：栈：先进后出，队列：先进先出。设队列为a=[1,2,3,4],设接收数数据的栈为stackin,设输出数据的栈为stackout。
		队列的push()操作就是在队为添加元素，pop()操作就是将队首的元素从队列中取出并删除。
思路：首先将队列a压入stackin中，即push操作；再弹出，即pop操作，而a.pop()=1,所以要将stackin逐个弹出并压入stackout中，将stackin中的“1
		压入stackout的尾部，再利用stackout.pop()将“1”取出。'''
class Solution:
	
		def __init__(self):
			self.stackin = []
			self.stackout = []
		def push(self, node):
			# write code here
			self.stackin.append(node)
		
		def pop(self):
			# return xx
			if self.stackout == []:
				while self.stackin:
					self.stackout.append(self.stackin.pop())
				return self.stackout.pop()
			return self.stackout.pop()

if __name__ == '__main__':
    s=Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    
    