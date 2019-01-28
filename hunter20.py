#t
n=input()
li=[]
for i in n:
    c=ord(i)
    b=c+3
    if b>90:
        b=b-26
    li.append(chr(b))
for i in li:
    print(i,end="")
