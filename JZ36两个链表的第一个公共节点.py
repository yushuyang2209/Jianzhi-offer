'''author: Shu YuTou Date:2020-7-27'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # if pHead1 == None or pHead2 == None:
        #     return None

        pTmp1 = pHead1
        pTmp2 = pHead2
        while pTmp1 and pTmp2:
            if  pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next
        
        if pTmp1: #phead1长，此时pTmp1还没有到表尾
            k =0    #记录两练表长度的差值
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1
            pTmp1 = pHead1
            pTmp2 = pHead2
            for i in range(k):
                pTmp1 = pTmp1.next
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
        
        if pTmp2:
            k =0
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1
            pTmp1 = pHead1
            pTmp2 = pHead2
            for i in range(k):
                pTmp2 = pTmp2.next
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
        
        
        # if lendiffval < 0:
        #     pTmp2 = pHead2
        #     # temp =  pHead2
        #     while lendiffval==0:
        #         pTmp2 = pTmp2.next
        #         lendiffval-=1
        #     # newhead = pTmp2
        #     pTmp1=pHead1
        #     while pTmp1:
        #         if pTmp1.next != pTmp2.next:
        #             pTmp1 = pTmp1.next
        #             pTmp2 = pTmp2.next
        #         else:
        #             return pTmp1.next
                    
        
                
if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n5 = ListNode(6)
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(7)
    l7 = ListNode(8)
    n1.next = n2
    n2.next = n3
    n3.next = l4
    # n4.next = l5
    
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    s = Solution()
    temp = s.FindFirstCommonNode(n1,l1)
    # len = ListNode.len(n1)
    print(temp)
    # print("______")
    # while n1:
    #     print(n1.val)
    #     n1= n1.next
    # print("______")
    # while l1:
    #     print(l1.val)
    #     l1= l1.next