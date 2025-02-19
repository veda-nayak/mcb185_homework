# 1, 1, 2, 3, 5
# take the last two values and sum them

n = 5
c = 0

a = 1
b = 1

print(a, b, sep=', ', end='')

for i in range(n):
    
    c = (a+b)
    
    print(",", c, end = '')
    
    a = b
    b = c
    