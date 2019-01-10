#r
n=int(input())
a=0
while(n>0):
    digit=n%10
    a=a+digit
    n=n//10
print(a)
