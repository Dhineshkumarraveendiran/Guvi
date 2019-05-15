#dsfgd
N=int(input())
L,R=input().split()
L=int(L)
R=int(R)
if (N in range(L+1,R)):
	print("yes")
else:
	print("No")
