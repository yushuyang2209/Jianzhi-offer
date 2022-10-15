'''author: Shu YuTou Date:2020/8/9'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        retnode=[]
        queue=[root]
        while queue:
            curnode = queue.pop(0)
            retnode.append(curnode.val)
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        return retnode