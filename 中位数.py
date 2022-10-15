'''author: Shu YuTou Date:2021/1/25'''
a=[1,3]
b=[2]
c=a+b
# print(c)
c.sort()
if len(c)%2==0:
	# print(len(c))
	s=(c[len(c)//2]+c[len(c)//2-1])/2
	print(s)
# print(s)
else:
	print(c[len(c)//2])


