#author: Shu YuTou Date:2020-7-19
class Solution:
    def jumpFloorII(self, number):
	    if number==1:
		    return 1
	    if number>1:
	        a=1
	        c=1
	        m=0
	        for i in range(2,number+1):
		        m=a*2*c
		        c=m

	    return m
		#或者
          # return pow(2,number-1)
if __name__ == '__main__':
    s=Solution()
    print(s.jumpFloorII(6))