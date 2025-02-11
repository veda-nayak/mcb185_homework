import random

trials = 1000000

'''
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

print("Another way:")
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

    print(dc, nor/trials, dis/trials, ad/trials)