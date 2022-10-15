#author: Shu YuTou Date:2020-7-20
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here

        # if pushV==[] or len(pushV)!=len(popV):
        #     return None
        # pushV.reverse()
        # for i in range(len(pushV)):
        #     if(pushV[i]==popV[i]):
        #         return True
        # return False
        
        #首先需要一个栈，列表
        #按照pushV的方式压入栈
        #弹出的时候需要弹出的时机，刚刚压入过后就判断
        #判断需要弹出的情况的条件，压入栈的顶部和弹出栈的顶部数据相等
        if pushV==[] or len(pushV)!=len(popV):
            return None
        stack=[]#新建一个栈
        index=0
        for item in pushV:
            stack.append(item)
            while (stack and stack[-1]==popV[index]):
                stack.pop()#弹出当前的栈顶
                index+=1
        if stack==[]:
            return True
        else:
            return False
            
                
            
        
        
        
    
if __name__ == '__main__':
    s=Solution()
    a=[1,2,3,4,5]
    b=[5,4,3,2,1]
    
    print(s.IsPopOrder(a,b))