#e
user_input = input ()
try:
   val = float(user_input)
   print("yes")
   
except ValueError:
   print("no")
