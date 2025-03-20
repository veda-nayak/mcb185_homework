import argparse
# import sys
import mcb185
import math


'''
parser = argparse.ArgumentParser(description = 'DNA entropy filter.')
parser.add_argument('fasta', type = str, help = 'name of fasta file')
parser.add_argument('--size', type = int, default = 4, help = 'window size [%(default)i]')
parser.add_argument('--entropy', type = float, default = 1.0, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action = 'store_true', help = 'mask with lowercase letters')

arg = parser.parse_args()

print('dusting with', arg.file, arg.size, arg.entropy)

seq = 'ATGCATGCGAGATATAGAGATAGAAAAAAAAAGGATAA'

def entropy(dna):
    count = {}
    H = 0
    
    for nt in dna:
        if nt not in count: count[nt] = 0
        count[nt] += 1
    
    for k, v in count.items():
        if v == 0: continue
        prob = v / len(dna)
        H += ( prob * math.log2(prob) )
    
    print(count)
    
    return -H

for defline, seq in mcb185.read_fasta(arg.fasta):
    mask = list(seq)
    for i in range(i - arg.size + 1):
        window = seq[i:i+arg.size]
        
        if entropy(window) < arg.entropy:
            if arg.lower: 
                for j in range(i, i+arg.size):
                    mask[j] = seq[j].lower()
                else: 
                    mask[j] = 'N'
print(''.join(mask))             
'''


def entropy(win):
    
    print(win.count('A'), win.count('T'), win.count('G'), win.count('C'))
    
    a = win.count('A')/len(win) # probability of a in the window
    c = win.count('C')/len(win)
    g = win.count('G')/len(win)
    t = win.count('T')/len(win)
    
    h = 0
    
    if a != 0: h += a * math.log2(a) 

    if t != 0:  h += t * math.log(t)
 
    if g != 0:  h += g * math.log(g)

    if c != 0: h +=  c * math.log2(c)

    
    
    
    return -h
    
print(entropy(seq))

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('fasta', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
# parser.add_argument('--size', type=int, default = 10, help='window size [%(default)i]' default = 10) # program now has optional parts to overwrite
parser.add_argument('--entropy', type=float, default = 1.4, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action = 'store_true')  # now it will do lowercase
parser.add_argument('--wrap', type=int, default = 80, help='wrap length [%(default)i]')
arg = parser.parse_args()

# Make a test data that will let you debug it --> make an easy fasta file to work with


for defline, seq in mcb185.read_fasta(arg.fasta): # arg.fasta gets you to the named arguments
    
    mask = list(seq) # turn it into a list because you can't edit strings
    
    for i in range(len(seq) - arg.size + 1): # windowing algorithm always looks the same
        window = seq[i:i+arg.size]
        
        if entropy(window) < arg.entropy: 
            # mask[i:i+arg.size] = 'N' # why can't I just do this --> makes the whole window into one thing
            
            for j in range(i, i + arg.size):
                if arg.lower: 
                    mask[j] = seq[j].lower()
                else: 
                    mask[j] = 'N'
                    
    print('>', defline, sep = '')    
    
    mask = ''.join(mask)
    for i in range(0, len(seq), arg.wrap): # another windowing algorithum to print in chunks
        print(mask[1:1+arg.wrap])
