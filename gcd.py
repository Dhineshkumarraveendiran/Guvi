#t
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a,b=input().split()
a=int(a)
b=int(b)
l=gcd(a,b)
print(l)
