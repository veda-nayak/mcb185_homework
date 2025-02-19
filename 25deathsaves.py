import random

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


# Old code below

'''

trial = 5 # sum of the next 3 variables
die = 0 # if you accumulate 3 failures
stable = 0 # 3 successes
revive = 0 # score 20

for i in range(trial):
    success = 0
    fail = 0
    print("trial", i)
    for i in range(5):
        r = random.randint(1,20)
        
        if r == 1: fail += 2
        elif r >= 2 and r < 10: fail += 1
        elif r >= 10: success += 1
        else: 
            revive += 1
            break
        
        if success == 3: 
            stable += 1
            break
            
        if fail == 3: 
            die += 1
            break
            
print("P(death):", die/trial)
print("P(stable):", stable/trial) 
print("P(revive):", revive/trial) 
        
'''