'''author: Shu YuTou Date:2020-7-25'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None and pHead2 == None:
	        return None
        if pHead1 == None:
	        return pHead2
        if pHead2 == None:
	        return pHead1
	        # 创建一个新的表头用于返回合并后的链表，比较两个链表的表头值的大小，确定newHead指向指小的那一个链表。
        newHead = pHead1 if pHead1.val < pHead2.val else pHead2

        pTmp1 = pHead1  # 指针1/循环变量1,用于遍历pHead1
        pTmp2 = pHead2  # 指针2/循环变量2，用于遍历pHead2

        prePointer = newHead  # 指针3/循环变量3,用于在两个链表之间跳转，由newHead决定其初始停靠点。

        # 根据newHead的指向，并将pTmp的后移一个，有两种情况。
        if newHead == pTmp1:
	        pTmp1 = pTmp1.next
        else:
	        pTmp2 = pTmp2.next
        # 开始遍历两个链表，当其中一个为空时结束。分两种情况

        while pTmp1 != None and pTmp2 != None:
	        if pTmp1.val <= pTmp2.val:
		        prePointer.next = pTmp1  # 此情况为pTmp1的值小于pTmp2的值，所以将prePointer指向当前的pTmp1
		        prePointer = pTmp1  # 将prePointer移动至当前pTmp1结点，作为下一次的表头
		        pTmp1 = pTmp1.next  # 将pTmp1移至下一个结点
	        else:
		        prePointer.next = pTmp2
		        prePointer = pTmp2
		        pTmp2 = pTmp2.next

        # 当上述循环结束时，判断哪一个链表先空，若pTmp1先空，说明跳转指针最后停在pTmp1的最后，
        # 那么直接将prePointer的下一跳指向当前的pTmp2
        if pTmp1 == None:
	        prePointer.next = pTmp2

        else:
	        prePointer.next = pTmp1

        return newHead  # 最后返回newHead