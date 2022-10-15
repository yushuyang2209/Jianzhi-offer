# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param proot TreeNode类 
# @param k int整型 
# @return int整型
#
import  builtins
class Solution:
    def KthNode(self , proot, k: int) -> int:
        proot1=builtins.list(proot)
        if len(proot1)<1:
            return -1
        for i in proot1:
            for j in range(0,len(proot1)-i-1):
                if proot1[j]>proot1[j+1]:
                    proot1[j] , proot1[j + 1]=proot1[j+1],proot1[j]
        return proot1[k-1]
if __name__ == '__main__':
    proot={5,3,7,2,4,6,8}
    proot1=list(proot)
    S=Solution()
    print(S.KthNode(proot1,3))





