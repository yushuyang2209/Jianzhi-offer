'''author: Shu YuTou Date:2020-7-24'''
'''题目：输入一个链表，输出该链表中倒数第k个结点。
# k如果比链表的长度大，返回None
# k如果比链表的长度小，可以定义两个变量，这两个变量中间间隔k
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def FindKthToTail(self, head, k):
		array = []
		while head!=None:
			array.append(head.val)
			head = head.next
		array.reverse()
		# ret = arraylist[k-1]
		if k>=1 and k<=len(array):
			ret=array[k-1]
			return ret
		else:
			return None
	 

if __name__ == '__main__':
	l1 = ListNode(1)
	l2 = ListNode(2)
	l3 = ListNode(3)
	l4 = ListNode(4)
	l1.next=l2
	l2.next=l3
	l3.next=l4
	l4.next=None
	s=Solution()
	print(s.FindKthToTail(l2,3))