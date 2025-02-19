# sum

total = 0
n = 10

for i in range(n):
    total += i
    
print(total)
    
    
# factorial

def factorial(n):
    total = 1

    for i in range(1,n):
        total *= (i)
        
    return total

print(factorial(3))

# n choose k

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))
    
print(choose(5,3))

# e

n = 1000

total = 0

for i in range(n):
    total += 1/factorial(i)
    
print(total)

# nilakantha series

n = 10

pi = 3
a = 2
b = a+1
c = b+1
switch = -1

for i in range(n):
    switch *= -1
    pi += switch * 4/(a*b*c)
    
    a = c
    b = a+1
    c = b+1
    
print(pi)

# triples

import math

n = 100

for a in range(1,n):
    for b in range(a , n):
        c  = math.sqrt(a**2 + b**2)
        if c % 1 == 0: print(a, b, int(c))

# saving throws
import random

def advantage():
    r1 = random.randint(1,20)
    r2 = random.randint(1,20)
    
    if r1 > r2: return r1
    return r2

def disadvantage():
    r1 = random.randint(1,20)
    r2 = random.randint(1,20)
    
    if r1 < r2: return r1
    return r2

def saving(d, n): # n = trials
    saves = 0
    adv = 0
    dis = 0
    
    for i in range(n):
        if random.randint(1,20) > d: saves += 1
        
    for i in range(n):
        if advantage() > d: adv += 1
        
    for i in range(n):
            if disadvantage() > d: dis += 1
    
    prob_norm = saves / n
    prob_adv = adv / n
    prob_dis = dis / n
    
    return prob_norm, prob_adv, prob_dis
    
print("5", saving(5, 100))
print("10", saving(10, 100))
print("15", saving(15, 100))

# death saves

n = 100
death = 0
stable = 0
revive = 0 

for i in range(n):
    fail = 0
    success = 0
    
    for i in range(5):
        
        r = random.randint(1,20)
        
        if r == 1: fail += 2
        elif r >= 2 and r < 10: fail += 1
        elif r >= 10: success += 1
        
        if r == 20: 
            revive += 1
            break        
 
        if success == 3: 
            stable += 1
            break

        if fail == 3:
            death += 1
            break
    
print("Deaths:", death/n)
print("Stable:", stable/n)
print("Revive:", revive/n)