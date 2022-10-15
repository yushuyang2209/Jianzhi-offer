'''author: Shu YuTou Date:2020/8/12'''
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	# 返回二维列表[[1,2],[4,5]]
	def Print(self, pRoot):
		if pRoot == None:return []
		stack1 = [pRoot]
		stack2 = []
		ret =[]
		while stack1 or stack2:
			if stack1:
				tmpret = []
				while stack1:
					tmpnode=stack1.pop(0)
					tmpret.append(tmpnode.val)
					if tmpnode.left:
						stack2.append(tmpnode.left)
					if tmpnode.right:
						stack2.append(tmpnode.right)
				ret.append(tmpret)
			if stack2:
				tmpret = []
				while stack2:
					tmpnode=stack2.pop(0)
					tmpret.append(tmpnode.val)
					if tmpnode.left:
						stack1.append(tmpnode.left)
					if tmpnode.right:
						stack1.append(tmpnode.right)
				ret.append(tmpret)
		return ret
if __name__ == '__main__':
	t1 = treeNode(1)
	t2 = treeNode(2)
	t3 = treeNode(3)
	t4 = treeNode(4)
	t5 = treeNode(5)
	t6 = treeNode(6)
	t1.left = t2
	t1.right = t3
	t2.left = t4
	t4.right = t5
	s = Solution()
	print(s.Print(t1))