#dtg
a=input()
count=0
for i in range(0,len(a)):
	if a[i]=="0" or a[i]=="1":
		count=count+0
	else:
		count=count+1
if count==0:
	print("yes")
else:
	print("no")
	
