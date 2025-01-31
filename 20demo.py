# TUPLE
print("TUPLE")

# When you want to pass back more than one thing from a function

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

'''
You always want to "unpack" the tupple

Good: mx, my = midpoint(1, 2, 3, 4)
BAD: m = midpoint(1, 2, 3, 4) --> mx = M[0], my = M[1]

'''
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

m = midpoint(1, 2, 3, 4)
print(m)
print(m[0], m[1])

# ITERATION
print("ITERATION")

'''
while <boolean expression is true>:
    do_something
'''

'''

Commented out to avoid my screen going crazy

while True:
    print('hello')
    
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
 
'''
triangular(3) = 1 + 2 + 3
triangular(4) = 1 + 2 + 3 + 4

~ factorial

'''

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