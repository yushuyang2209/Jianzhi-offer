'''author: Shu YuTou Date:2020-7-25'''
# -*- coding:utf-8 -*-
'''题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）'''
'''思路：在给出链表的每个节点处都复制一下，并连接起来，再把相同节点之间的链接断开。
如原始链表为：1->2->3->4->None,则复制后的链表为1->1->2->2->3->3->4->4->None，然后再断开1->2->3->4->None，1->2->3->4->None'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
# import copy
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        '''第一步：复制一个一样的node,并添加到之前的链表的每一个node（节点）的后面'''
        pTmp1 = pHead  # 在原始的链表上移动
        while pTmp1:
            copynode = RandomListNode(pTmp1.label)
            copynode.next = pTmp1.next
            pTmp1.next = copynode
            pTmp1 = copynode.next  # pTmp = pTmp.next.next 移动pTmp1指针
        '''第二步：根据原始各节点random的指向，实现新建的random的指向。新建节点的random与原始该节点的random指向的next对齐.
            注意:循环时，指针指向None的情况。如line31'''
        # 实现新建的random的指向
        pTmp2 = pHead  # 在原始的链表上移动
        while pTmp2:
            if pTmp2.random:
                pTmp2.next.random = pTmp2.random.next
            pTmp2 = pTmp2.next.next
        '''第三步： 断开原来的node和新的node之间的链接，断开后自动分成两个链表。
            注意:循环时，两个指针指向None的情况。如line41,line43'''
        # 断开原来的node和新的node之间的链接
        pTmp3 = pHead
        newHead = pHead.next    #重新定义一个变量，用于记录复制后链表头的位置，不让他循环
        pNewTmp = pHead.next    #在复制后的链表头上定义一个指针，用于在复制后的链表中循环
        while pTmp3:
            if pTmp3.next:
                pTmp3.next = pTmp3.next.next
            if pNewTmp.next:
                pNewTmp.next = pNewTmp.next.next
            pTmp3 = pTmp3.next  #在原始链表上移动
            pNewTmp = pNewTmp.next  #在新的链表上移动
        return newHead
if __name__ == '__main__':
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    s=Solution()
    temp = s.Clone(n1)
    while temp:
        print(temp.label)
        temp =temp.next
    
    



