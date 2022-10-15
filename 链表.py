'''author: Shu YuTou Date:2020-7-23'''
class Node():
     def __init__(self, x):
         self.val = x
         self.next = None
class Singlelinklist():
	def __init__(self,node=None):
		self.__head=node
		#打印链表的长度
	def lenglist(self):
		cur = self.__head
		count = 0
		while cur is not None:
			cur = cur.next
			count += 1
		print('\n',count)
		#头部插入
	def headadd(self,val):
	     node = Node(val)
	     node.next =self.__head
	     self.__head = node
		#尾部插入
	def tailadd(self,val):
		node = Node(val)
		cur = self.__head
		if cur is None:
			self.__head = node
		else:
			while cur.next is not None:
				cur = cur.next
			cur.next = node
		#中间插入
	def middeladd(self,val,position):
		node = Node(val)
		if position<=0:  #位置信息为负数的话，认为用户是想在头节点插入
			self.headadd(val)
		else:
			cur = self.__head
			for i in range(position-1):
				cur = cur.next
			node.next = cur.next
			cur.next = node
	#删除链表中间的某一项
	def delete(self,position):
		if position < 0:
			print("删除项所在位置信息输入错误")
		cur = self.__head
		for i in range(position-1):
			cur = cur.next
		tmp = cur.next.next
		cur.next.next = None
		cur.next = tmp
		#查找一点节点是否存在
	def searchnode(self,val):
		node = Node(val)
		cur = self.__head
		while cur is not None:
			if cur == node:
				return True
			cur = cur.next
		return False
		
	
		#打印整个链表
	def walkthrough(self):
		cur = self.__head
		while cur:
			print(cur.val,end=" ")
			cur = cur.next
   
alink =Singlelinklist()
# alink.headadd(1)
# alink.headadd(2)
# alink.headadd(3)
# alink.tailadd(4)
# alink.tailadd(5)
# alink.tailadd(6)
for i in range (0,10):
	alink.tailadd(i)
# alink.middeladd(10,2)
print(alink.searchnode(9))
# def printChain(node):
#     while node:
#         print(node.value)
#         node = node.next
# if __name__ == '__main__':
#     #1->2->3->None
#     # l1 = ListNode(1)
#     # print(ListNode(2).value)
#     # l2 = ListNode(2)
#     # l3 = ListNode(3)
#     # l3.next=l2
#     # l2.next=l1
#     # l1.next=None
#     # printChain(l3)
#     for i in range(0,10):
#         q = i
#
#         q = q.next
#     printChain(q)