import mcb185
import sequence 

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10

for i in range(len(seq) - w + 1): # range for a window is length - window size + 1
    s = seq[i:i+w]
    print(i, sequence.gc_comp(s), sequence.gc_skew(s))