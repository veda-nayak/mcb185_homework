import mcb185
import sys
import gzip

def find_cds(seq):
    translation = mcb185.translate(seq)
    start = -1
    stop = -1
    
    for i in range(0, len(translation)):
        if translation[i] == 'M':
            start = i
            break
        else: continue
        
    for i in range(0, len(translation)):
        if translation[i] == '*':
            stop = i
            break
        else: continue
    
    if start != -1 and stop != -1: return translation[start:stop]

path = sys.argv[1]
min_length = int(sys.argv[2])
    
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    
    seq_rev = []
    for i in range(0, len(seq)):
        seq_rev.append(seq[i])
    
    seq_rev.reverse()
    
    for i in range(0, len(seq_rev)):
        if seq_rev[i] == 'A':   seq_rev[i] = 'T'
        elif seq_rev[i] == 'C': seq_rev[i] = 'G'
        elif seq_rev[i] == 'G': seq_rev[i] = 'C'
        elif seq_rev[i] == 'T': seq_rev[i] = 'A'
    
    seq_rev = ''.join(seq_rev)
    
    for i in range(0, 3):
        if find_cds(seq[i:len(seq)-1]) != None:
            if len(find_cds(seq[i:len(seq)-1])) >= min_length:
                print(">", defwords[0], sep = '')
                print(find_cds(seq[i:len(seq)-1]))
    
    for i in range(0, 3):
        if find_cds(seq_rev[i:len(seq_rev)-1]) != None:
            if len(find_cds(seq_rev[i:len(seq_rev)-1])) >= min_length:
                print(">", defwords[0], sep = '')
                print(find_cds(seq_rev[i:len(seq_rev)-1]))   