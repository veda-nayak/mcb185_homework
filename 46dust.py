# Low entropy: ...AAAAAAAAAAAAAAAAA...
# Low complexity: ...ACACACACACACACAC...

# Mask out these regions and turn them into N's

# Shannon entropy: H = - SUMATION( p_i * log_2 (p_i) ) --> complexity
# H = 2 , 2 bits, you would need 2 coins to get all the combinations
    # A - 00
    # T - 01
    # G - 10
    # C - 11
    
import sys
import math
import mcb185

def entropy(seq): # - Σ (p(x) * log2(p(x)))
    
    a = seq.count('A') / len(seq) # probabilities
    c = seq.count('C') / len(seq) 
    g = seq.count('G') / len(seq) 
    t = seq.count('T') / len(seq) 

    H = 0
    
    if a != 0: H -= a * math.log2(a)
    if c != 0: H -= c * math.log2(c)
    if g != 0: H -= g * math.log2(g)
    if t != 0: H -= t * math.log2(t)

    return H

path = sys.argv[1]
k = int(sys.argv[2])
threshold = float(sys.argv[3])


for defline, seq in mcb185.read_fasta(path):
    
    mask = list(seq)
    
    for i in range(len(seq) - k + 1):
        window = seq[i:i+k]

        H = entropy(window)
        
        if H < threshold: 
            for j in range(i, i+k):
                mask[j] = 'N'
                # mask[j] = seq[j].lower()
    
print(''.join(mask))
            
        
        