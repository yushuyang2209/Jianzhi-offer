'''author: Shu YuTou Date:2020/8/11'''
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack1 = [pRoot]
        stack2 = []
        ret = []
        while stack1 or stack2:
            if stack1:
                tempret=[]
                while stack1:
                    tempNode=stack1.pop()
                    tempret.append(tempNode.val)
                    if tempNode.left:
                        stack2.append(tempNode.left)
                    if tempNode.right:
                        stack2.append(tempNode.right)
                ret.append(tempret)
            if stack2:
                tempret=[]
                while stack2:
                    tempNode = stack2.pop()
                    tempret.append(tempNode.val)
                    if tempNode.right:
                        stack1.append(tempNode.right)
                    if tempNode.left:
                        stack1.append(tempNode.left)
                ret.append(tempret)
        return ret
if __name__ == '__main__':
    t1 = treeNode(1)
    t2 = treeNode(2)
    t3 = treeNode(3)
    t4 = treeNode(4)
    t5 = treeNode(5)
    t6 = treeNode(6)
    t7 = treeNode(7)
    t8 = treeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t4.right = t5
    s = Solution()
    print(s.Print(t1))
