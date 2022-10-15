'''author: Shu YuTou Date:2020-7-23'''
#链表的结构
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, listnode):
        self.value = listnode
        self.next = None


def printChain(node):
    while node:
        print(node.value)
        node = node.next

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        arraylist = []
        while listNode:
            arraylist.append(listNode.value)
            listNode = listNode.next
        arraylist.reverse()
        return arraylist[0]

if __name__ == '__main__':
    # 1->2->3->None
    l1 = ListNode(1)
    # print(ListNode(2).value)
    l2 = ListNode(2)
    # l3 = ListNode(3)
    l1.next = l2
    # l2.next = l3
    # l3.next = None
    
    printChain(l1)
    print("--------")
    # printChain(l3)
    s=Solution()
    print(s.printListFromTailToHead(l1))