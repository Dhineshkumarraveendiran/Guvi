#h
a,b =input().split()
a =int(a)
b=int(b)
 
for n in range(a,b+1):
   
   sum = 0
 
   
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if n==sum:
       print(n,end=' ')
