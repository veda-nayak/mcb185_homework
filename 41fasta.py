#the list variation one is giving something wrong

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))
    
    # defline --> chr. number + nt. numbers
    # seq prints out sequence in designated amount
    # len(seq) = number nucleotides in the chr. 

A = 0
a = 'A'
C = 0
c = 'C'
G = 0
g = 'G'
T = 0
t = 'T'
N = 0 
n = 'N'

print("name", "P(A)", "P(C)", "P(G)", "P(T)", "P(N)", sep = "             ")
''' 
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    for nt in seq:
        if nt == a:   A += 1
        elif nt == c: C += 1
        elif nt == g: G += 1
        elif nt == t: T += 1
        else:         N += 1
    
    print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))


print("name", "P(A)", "P(C)", "P(G)", "P(T)", "P(N)", sep = "             ")
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    counts = [0,0,0,0,0] # A C G T N/len
    defwords = defline.split()
    name = defwords[0]
    
    for nt in seq:
        if nt == a:   counts[0] += 1
        elif nt == c: counts[1] += 1
        elif nt == g: counts[2] += 1
        elif nt == t: counts[3] += 1
        else:         counts[4] += 1
        
    print(name, end = ' ')
    for n in counts: print(n/len(seq), end = ' ')
    print()
'''

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    
    nts = 'ACGTN'
    counts = [0] * len(nts)

    for nt in seq:           # for the nt in the sequence
        index = nts.find(nt) # see if is a nucleotide we're counting and find which index it is (ex. G = index 2)
        counts[index] += 1   # add one to that index output

    print(name, end = ' ')
    for n in counts: print(n / len(seq), end = ' ')
    print()
    
    # note: if unknown letter, index = -1 --> N
    
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    
    for nt in 'ACGTN':
        print(seq.count(nt) / len(seq), end = '     ')
    print()