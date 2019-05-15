#dgd
s=input()
vow=set('aeiou')
if not vow.isdisjoint(s):
    print("yes")
else:
    print("no")
