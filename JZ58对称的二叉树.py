'''author: Shu YuTou Date:2020/8/10'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismirror(left,right):
	        if left == None and right == None:
		        return True
	        if left == None or right == None:
		        return False
	        if left.val != right.val:
		        return False
	        ret1 = ismirror(left.left,right.right)
	        ret2 = ismirror(left.right,right.left)
	        return ret1 and ret2

        if root == None:
	        return True
        return ismirror(root.left,root.right)