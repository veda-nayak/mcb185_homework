import math
def dist2(x1, y1, x2, y2):
    a = float(x2) - float(x1)
    b = float(y2) - float(y1)
    
    c = math.sqrt(a**2 + b**2)
    
    print("The distance between these points is", c)
    
dist2(0, 0, 3, 4)

def valid_prob(p):
    p = float(p)
    if (p <= 1) and (p >= 0): print("You're good!")
    else: print("No that's bad")

valid_prob("0.5")
valid_prob("1.3")

def geometric_four(a, b, c, d):
    product = (a*b*c*d)
    mean = math.pow(product,1/4)
    print(mean)

geometric_four(1, 2, 3, 4)