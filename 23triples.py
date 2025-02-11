import math
  
  
limit = 100
  
for a in range(1, limit):
    for b in range(a, limit): # only check numbers higher than yourself
        c = math.sqrt(a**2 + b**2)
        # could also do if c % 1 == 0: print(a, b, int(c))
        if int(c) == c: print(a, b, int(c))
        