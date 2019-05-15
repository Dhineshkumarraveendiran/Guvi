#dfd
n,m=map(int,input().split())
a=n*m
li=[]
for i in range(0,9):
	u=i*i
	li.append(u)
if(a in li):
	print("yes")
else:
	print("no")
