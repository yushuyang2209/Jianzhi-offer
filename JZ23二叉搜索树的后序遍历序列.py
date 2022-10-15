'''author: Shu YuTou Date:2020/8/9'''
'''二叉搜索树：）它或者是一棵空树，或者是具有下列性质的二叉树： 
		若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
		若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉搜索树'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence==[]:
            return True
        rootNum = sequence.pop()
        index = None
        for i in range(len(sequence)):
            if index == None and sequence[i] > rootNum:
                index = i
            if index != None and sequence[i] < rootNum:
                return False
        leftret = self.VerifySquenceOfBST(sequence[:index])
        rightret = self.VerifySquenceOfBST(sequence[index:])
        return leftret and rightret