'''author: Shu YuTou Date:2020/8/9'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        def midtravel(cur):
            if cur == None: return
            midtravel(cur.left)

            if self.pre == None:
                self.head = cur
            else:
                self.pre.right = cur
                cur.left = self.pre
            self.pre = cur

            midtravel(cur.right)

        if pRootOfTree == None: return
        self.pre = None
        midtravel(pRootOfTree)
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head
