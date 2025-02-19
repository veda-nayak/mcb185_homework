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

# METHOD 1 FROM CLASS

'''
trials = 100

def advantage():
    r1 = random.randint(1,20)
    r2 = random.randint(1,20)
    return max(r1, r2)
    
def disadvantage():
    r1 = random.randint(1,20)
    r2 = random.randint(1,20)
    return min(r1, r2)




#standard
print("Standard:")
for dc in range(5 , 16 , 5):
    success = 0
    for i in range(trials):
        roll = random.randint(1,20)
        if roll > dc: success += 1

    print(dc, success/trials)


# advantage
print("Advantage:")
for dc in range(5 , 16 , 5):
    success = 0
    for i in range(trials):
        roll = advantage()
        if roll > dc: success += 1

    print(dc, success/trials)
    
# disadvantage
print("Disadvantage:")
for dc in range(5 , 16 , 5):
    success = 0
    for i in range(trials):
        roll = disadvantage()
        if roll > dc: success += 1

    print(dc, success/trials)
'''

# METHOD 2 FROM CLASS

'''

sides = 20
for dc in range(5 , 16 , 5):
    nor = 0
    ad = 0
    dis = 0
    for i in range(trials):
        r1 = random.randint(1, sides)
        r2 = random.randint(1, sides)
        if r1 >= dc: nor += 1
        if r1 >= dc and r2>= dc: dis += 1
        if r1 >= dc or r2>= dc: ad += 1

    print(dc, nor/trials, ad/trials, dis/trials)

'''
    
