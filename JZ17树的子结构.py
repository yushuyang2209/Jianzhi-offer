'''author: Shu YuTou Date:2020/8/9'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, A, B):
	    if not A or not B:
		    return False

	    # 判断根节点：以节点A为根节点的子树包含树B
	    def isChild(A,B):
	        if not B:
		        return True
	        if not A or A.val != B.val:
		        return False
	        if isChild(A.left,B.left) and isChild(A.right,B.right):
		        return True
	        return False

	    # 判断根节点：以节点A为根节点的子树包含树B
	    if isChild(A,B):
		    return True
	    # 判断A左、右子树是否包含树B
	    if self.HasSubtree(A.left,B) or self.HasSubtree(A.right,B):
		    return True
	    return  False