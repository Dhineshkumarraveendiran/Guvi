#dfgvd
import re
z=input()
if (re.findall('[a-zA-Z]',z) )and( re.findall('[0-9]',z)):
    print("Yes")
else: 
    print("No")
