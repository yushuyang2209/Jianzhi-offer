'''author: Shu YuTou Date:2020/8/12'''
'''二叉搜索树的中序遍历，即为从大到小排序'''
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # def breadth_travel(root):
        #     if root is None:
        #         return None
        #     queue = [root]
        #     res = []
        #     while queue:
        #         cur_node = queue.pop(0)
        #         res.append(cur_node.val)
        #         if cur_node.left is not None:
        #             queue.append(cur_node.left)
        #         if cur_node.right is not None:
        #             queue.append(cur_node.right)
        #     return res
        # if pRoot == None  or k == 0:
        #     return
        # treelist = breadth_travel(pRoot)
        # treelist.sort()
        # return treelist[k-1]
        retList=[]
        def preorder(root):
            if root == None:
                return None
            preorder(root.left)
            retList.append(root.val)
            preorder(root.right)
        preorder(pRoot)
        if len(retList)<k or k <1:
            return
        return retList[k-1]
if __name__ == '__main__':
    t1 = treeNode(3)
    t2 = treeNode(1)
    t3 = treeNode(4)
    t4 = treeNode(2)
  
    t1.left =t2
    t1.right = t3
    t2.left =None
    t2.right = t4
    s =Solution()
    print(s.KthNode(t1,1))
