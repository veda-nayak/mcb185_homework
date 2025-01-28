# Unit 1 Practice Questions

# Practice
## F to C

def f2c(f): 
    c = (f - 32) * ( 5 / 9 )
    print(f, "degrees F is equal to", c, "degrees C")

f2c(50)
f2c(80)
f2c(100)
f2c(98.6)

## MPH to KPH

def m2k(m):
    k = 1.609 * m
    print(m, "MPH is equal to", k, "KPH")

m2k(17)    

## Don't be MEAN
a = 1
b = 2
c = 3

def mean3(a, b, c):
    add = a + b + c
    mean = add / 3
    print("The mean of", a, ",", b, ", and", c, "is", mean)
    return mean

mean3(a, b, c)

def harmonicmean(a, b, c):
    mean = 3 / ( (1/a) + (1/b) + (1/c))
    print("The harmonic mean of", a, ",", b, ", and", c, "is", mean)
    return mean

harmonicmean(a, b, c)

print( "The difference between the arithmetic and harmonic mean is", (mean3(a, b, c) - harmonicmean(a, b, c)))

def geomean(a, b, c):
    y = 1/3
    x = a * b * c
    mean = pow(x, y)
    print("The geometric mean of", a, ",", b, ", and", c, "is", mean)

geomean(a, b, c)

## distance between 2 points
def dist2(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    
    import math
    c = math.sqrt(a**2 + b**2)
    print("The distance between these points is", c)
    
dist2(0, 0, 3, 4)

## DNA concentration given OD260
def concentration(x): print("Your DNA concentration is:", 50*x)
concentration(20)

# More practice

# Assessment Example

def comp(nt):
    if nt == 'A': print('T')
    elif nt == 'T': print('A')
    elif nt == 'C': print('G')
    elif nt == 'G': print('C')
    else: print("None")

comp('A')
comp('T')
comp('C')
comp('G')
comp('pancakes')