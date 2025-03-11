# FINSIH
import sys

# python3 45colorname.py ~/Code/MCB185/data/colors_extended.tsv

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p-q)
    return d

R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

rbg = [R, G, B]

colorfile = sys.argv[1]

minimum = [(256*3), 'name'] 

with open(colorfile) as fp:
    for line in fp:
        identity = line.split()

        name = identity[0]
        code = identity[2]
        
        rgb_new = code.split(',')
        rgb_new[0] = int(rgb_new[0])
        rgb_new[1] = int(rgb_new[1])
        rgb_new[2] = int(rgb_new[2])
    
        distance = dtc(rbg, rgb_new)
        
        if distance < minimum[0]:
            minimum[0] = distance
            minimum[1] = name
        
print(minimum[1])

sys.exit()



















# treat them like coorinates in 3D space
# absolute distance of R's vs. G's vs. B's --> take total sum of the absolute differences and take lowest
# Turn values into probabilities, use kalbek-libel distance to compare the histograms

# each time check if this is the minimum, if yes save the values, if not ignroe


# Assessment example
# could also use random.randint()
'''
limit = 64
n = 0
for r in range(limit):    
    for g in range(limit):
        for b in range(limit):
            n += 1
print(n)
'''
limit = 40
n = 0
import random 
colors = set()
while True:
    r = random.randint(0, limit - 1)
    g = random.randint(0, limit - 1)
    b = random.randint(0, limit - 1)
    
    n += 1
    colors.add( (r, g, b) )
    
    if len(colors) == limit**3: break
    
print(n)
    
    
    


