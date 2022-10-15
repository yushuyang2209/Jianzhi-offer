'''author: Shu YuTou Date:2020/8/10'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
# 1.寻找右字树，如果存在就一直寻找到右字树的最左节点就是下一个节点
# 2.没有右字树，就寻找他的父节点，一直找到它是父节点的左子树，打印父节点
	if pNode.right:
		res = pNode.right
		while res.left:
			res = res.left
		return res
	else:
		tmpnode = pNode
		while tmpnode.next:
			if tmpnode.next.left == tmpnode:
				return tmpnode.next
			tmpnode = tmpnode.next
		return None