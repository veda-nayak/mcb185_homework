# TUPLE
# When you want to pass back more than one thing from a function

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

'''
You always want to "unpack" the tupple

Good: mx, my = midpoint(1, 2, 3, 4)
BAD: m = midpoint(1, 2, 3, 4) --> mx = M[0], my = M[1]


mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

m = midpoint(1, 2, 3, 4)
print(m)
print(m[0], m[1])

# ITERATION
print("ITERATION")


while <boolean expression is true>:
    do_something
'''

'''

Commented out to avoid my screen going crazy

while True:
    print('hello')
    
'''

'''
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break    # break statement

# better way to make a break statement below

print("The better way")

i = 0
while i < 3:
    i = i + 1
    print('hey', i)
    
print("For as long as you hand me bills I will keep taking them")
i = 1
while i < 10:
    print(i)
    i = i + 3
 
# better way to make a break statement below

print("The better way. Issue: need to know how times you need. You know how much money the bro has")
for i in range(1, 10, 3):
    print(i)
 

triangular(3) = 1 + 2 + 3
triangular(4) = 1 + 2 + 3 + 4

~ factorial



# My way

print("What I tried myself")

def triangular(n):
    i = 0
    while i <= n:
        i = i + 1
    print("The triangular of", n, "is equal to", i)

triangular(3)
triangular(4)

def factorial(n):
    i = 0
    product = 1
    while i < n:
        i = i + 1
        product = product*i
    print(n, "factorial is equal to", product)

factorial(1)
factorial(3)
factorial(4)

# What Korf did

print("Korf's answer")

def triangular(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    print("The triangular of", n, "is equal to", i)

triangular(3)
triangular(4)

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    print(n, "factorial is equal to", product)

factorial(1)
factorial(3)
factorial(4)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print("I want", thing)

for i in range(len(basket)):
    print("I want", basket[i])
    
def even_or_odd(n):
    for i in range(n):  # this does numbers 0 - (n-1)
        if i % 2 == 0: print(i, 'is even')
        else: print(i, "is odd")
        
even_or_odd(7)
even_or_odd(5)

# RANDOM NUMBERS
print("RANDOM NUMBERS")

import random

r = random.randint(1, 6) # inclusive of the endpoint


total = 0
for i in range(1001):   # outside loop is i
    threed6 = 0
    for j in range(3):  # inside loop is j
        r = random.randint(1, 6)
        threed6 += r
    total += threed6
        # print(r)
        # print(threed6)

print("The average of 1000 six-sided dice is", total/1000)

# Practice problems

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

print(factorial(3))

def euler(n):   # e = 1 + 1/n!
    e = 1
    for i in range(1, n+1):
        e += 1 / factorial(i)
    return e
        
print(euler(1000))


import math

e = 0
n = 0
while e - math.e < 4.440892098500626e-16: # while True for infinite
        e += 1 / factorial(n)
        n += 1
        print(e, e - math.e)

def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i 
    return product
      
def poisson(n, k):
    TEXT

def nCk(n, k):
    value = factorial(n) / ( factorial(k) * factorial(n - k) )
    return value

print(nCk(3, 4))

def is_prime(n):
    for d in range(2, n//2):
        if n % d == 0: return False
    return True # need to check every number before you say true so keep it outside the loop

print(is_prime(8))
print(is_prime(31))

'''

'''
# MONTY PI-THON

import random

inside = 0
outside = 0
total = 0

while True:
    
    x = random.random()
    y = random.random()
    
    distance = (x**2 + y**2)**0.5
    
    if distance <= 1: inside += 1

    total += 1
    print( 4 * inside / total )
    
'''
'''
# D&D Stats

import random
die_4 = random.randint(1,6)
 

# 3D6
sum_die = 0
count = 0
for i in range(10):
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    die_3 = random.randint(1,6)
    total = die_1 + die_2 + die_3
    sum_die += total
    count += 1

avg = sum_die / count 
print(avg)
   

# 3D6r1

total = 0
count = 0
for i in range(10000):
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    total += r1 + r2 + r3
    count += 1
    
    if die_1 == 1: die_1 = random.randint(1,6)
    elif die_2 == 1: die_2 = random.randint(1,6)
    elif die_3 == 1: die_3 = random.randint(1,6)
    
avg = total / count
print(avg)

# 3D6x2

def max_2d():
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    if r1 > r2: return r1
    else: return r2
    
count = 0
total = 0
for i in range(10000):
    r1 = max_2d()
    r2 = max_2d()
    r3 = max_2d()
    total += r1 + r2 + r3
    count += 1

avg = total / count
print(avg)

# Loaded die

def loaded_die():
    r = random.random()
    if r < 0.1: return 1
    if r < 0.2: return 2
    if r < 0.3: return 3
    if r < 0.4: return 4
    if r < 0.5: return 5
    return 6

for i in range(10):
    print(loaded_die())
    
'''

sign = -1
pi_approx = 3

n1 = 2
n2 = n1 +1
n3 = n2 + 1

for i in range(100000):
    
    sign *= -1
    
    pi_approx += sign * ( 4 / (n1 + n2 + n3) )
    
    
    
    n1 = n3
    n2 = n1 +1
    n3 = n2 + 1

print(pi_approx, n1, n2, n3, sign)
    