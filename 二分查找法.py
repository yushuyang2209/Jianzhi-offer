'''author: Shu YuTou Date:2020-7-22'''
'''查找的数列必须有序'''
def bSearch(array,target):
	left = 0 #数列的头
	right=len(array)-1 #数列的尾
	while left <= right:
		mid = (left+right)//2 #获得数列的中间位置
		if array[mid]==target:
			return mid
		elif array[mid]<target:
			left = mid + 1
		else:
			right= mid - 1
	return None
if __name__ == '__main__':
    ret=bSearch([1,2,3,4,5],5)
    print(ret)