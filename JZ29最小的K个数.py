'''author: Shu YuTou Date:2020/8/10'''
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        '''方法一：排序'''
        # if tinput == None:return []
        # if k>len(tinput):
        #     return[]
        # tinput.sort()
        # return tinput[:k]
        '''方法二：堆
        Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前k小值。'''
        if  tinput == None or len(tinput)<k or k==0:
            return
        hp = []
        for x in tinput[:k]:
            hp.append(-x)
        # hp = [-x for x in arr[:k]]
        heapq.heapify(hp)               #将hp列表转化为堆

        for i in range(k,len(tinput)):
            if -hp[0] > tinput[i]:
                # heapq.heappop(hp)
                heapq.heappushpop(hp,-tinput[i])#弹出hp堆里面的最小值,并把当前值放置到hp中
        ans=[]
        for x in hp:
            ans.append(-x)
        # ans = [-x for x in hp]
        return ans
if __name__ == '__main__':
    s = Solution()
    arr = [4,5,1,6,2,7,3,8]
    print(s.GetLeastNumbers_Solution(arr,4))


