import sys
import mcb185
import itertools
import math

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    
    rev_seq = list(seq)
    for i in range(0, len(rev_seq)):
        if rev_seq[i] == 'A':   rev_seq[i] = 'T'
        elif rev_seq[i] == 'C': rev_seq[i] = 'G'
        elif rev_seq[i] == 'G': rev_seq[i] = 'C'
        elif rev_seq[i] == 'T': rev_seq[i] = 'A'
    
    rev_seq.reverse()
    rev_seq = "".join(rev_seq)
     
    kcount = {}
    for k in range(1, math.ceil(((len(seq) / 2) + 1))):
        for i in range(0, len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer not in kcount: kcount[kmer] = 0
            kcount[kmer] += 1
        for i in range(1, len(rev_seq) - k + 1):
            kmer = rev_seq[i:i+k]
            if kmer not in kcount: kcount[kmer] = 0
            kcount[kmer] += 1
        
        missing = {}
        found = 0
        for nts in itertools.product('ATGC', repeat = k):
            kmer = ''.join(nts)
            if kmer in kcount: 
                found += 1
            else: 
                missing[kmer] = 0
                   
        if len(missing) != 0: 
            print('k = ', k, sep = '')
            print('Number of missing kmers = ', len(missing), sep = '')
            break