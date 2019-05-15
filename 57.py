#dxf
n,k=input().split()
n=int(n)
k=int(k)
s=0
m=[int(i) for i in input().split()]
for i in range(0,n):
	if(k==m[i]):
		s=s+1
print(s)
