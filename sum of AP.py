#r
def  sumOfAP(a,  d,  n): 
    sum = (n // 2) * (2 * a + (n - 1) * d) 
    return sum
      
a,d,n=input().split()  
a =int(a)
d =int(d) 
n =int(n) 
  
print(sumOfAP(a, d, n)) 
