'''author: Shu YuTou Date:2020-8-5'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if pre == None or tin == None:
            return None
        if len(pre) or len(tin):
            return None
        root = pre[0]
        rootNode = TreeNode(root)#新建一个根节点节点
        pos = tin.index(root)

        tinLeft = tin[:pos]
        tinRight = tin[pos+1:]

        preLeft = pre[1:pos+1]
        preRight = pre[pos+1:]
        #寻找字树
        rootleft =  self.reConstructBinaryTree(preLeft,tinLeft)
        rootright = self.reConstructBinaryTree(preRight,tinRight)

        rootNode.left = rootleft
        rootNode.right = rootright
        return rootNode