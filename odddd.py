#r
start, end =input().split()
start=int(start)
end=int(end)
  
# iterating each number in list 
for num in range(start+1, end + 1): 
      
    # checking condition 
    if num % 2 != 0: 
        print(num, end = " ") 
