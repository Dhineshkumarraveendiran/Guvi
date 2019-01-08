#li
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
elif a==b>c:
    print(a)
else:
    print(c)
