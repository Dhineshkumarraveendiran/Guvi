#r
def check_pangram(arg):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0 :
    return True
  return False
u = input()
if(check_pangram(u)):
  print("yes")
else:
  print("no")
