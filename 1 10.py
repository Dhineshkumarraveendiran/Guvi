#r
N,K=map(int,input().split())
a=list(map(int,input().split()))
sum1=0
for i in range(0,K):
	sum1=sum1+a[i]
print(sum1)
