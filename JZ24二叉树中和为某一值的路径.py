'''author: Shu YuTou Date:2020/8/9'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		res = []
		path = []
		def recur(rootNode,tarNum):
			if rootNode == None:return []
			path.append(rootNode.val)
			tarNum = tarNum - rootNode.val
			if tarNum == 0 and not rootNode.left and not rootNode.right:
				res.append(list(path))
			recur(rootNode.left,tarNum)
			recur(rootNode.right,tarNum)
			path.pop()
		recur(root,expectNumber)
		return res


