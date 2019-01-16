#r
Number = int(input())


First_Value = 0
Second_Value = 1
           

for Num in range(1, Number+1):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next,end=' ')
