'''author: Shu YuTou Date:2020-7-24'''
'''输入一个链表，反转链表后，输出新的链表的表头
思路：以单链表的第二个元素为循环变量，用两个变量循环向后操作，并设置1个辅助变量temp,保存数据。'''
class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead==None:
            return None
        # if pHead.next==None:
        #     return pHead
        #'''不可以用pHead来遍历列表，否则会丢失列表的一些节点 ，
        # 可以使用和head相同类型的临时的指针变量，这个变量p1先初始化为链表结构的pHead指针'''
        p1 = pHead      #循环变量1
        p2 = pHead.next     #循环变量2
        temp = None     #保存下一个结点地址的临时变量
        #每两个节点一个移动一次
        while p2:
            temp = p2.next #如果不加这一句，p2.next这个节点以及后面的节点都将会消失，因为前两个节点倒置后，后面的节点会断开。
            p2.next = p1   #倒置
            #移动两个循环变量的位置p1->p2;p2->temp
            p1 = p2
            p2 = temp
        pHead.next = None   #所有节点倒置完成后，原先的头结点应当指向None
        return p1 #因为当p1,p2移动最后尾节点时，最后的节点指向None，
                # 即此时，p2.next=None,所以当此次（最后一次）循环后，p2=none,所以应当返回p1。
        '''递归'''
        # if pHead==None or pHead.next == None:
        #     return pHead
        # newhead = self.ReverseList(pHead.next)
        # pHead.next.next = pHead
        # pHead.next = None
        # return newhead

if __name__ == '__main__':
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    s=Solution()
    print(s.ReverseList(l1))