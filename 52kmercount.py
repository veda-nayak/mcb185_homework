import sys
import mcb185
import itertools

k = int(sys.argv[2])

kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    
    for i in range(0, len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in kcount: kcount[kmer] = 0
        kcount[kmer] += 1
        
    print(">", defline.split()[0], sep = '')
    # for kmer, n in kcount.items():
        # print(kmer, n)

    for nts in itertools.product('ATGC', repeat = k):
        new_kmer = ''.join(nts)
        if new_kmer in kcount: print(new_kmer, kcount[new_kmer])
        print(new_kmer, 0)












'''
k = int(sys.argv[2])

kcount = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        
        if kmer not in kcount: kcount[kmer] = 0
        kcount[kmer] += 1

for kmer, n in kcount.items(): 
    print(kmer, n)
    
for nts in itertools.product('ACGT', repeat = k):
    kmer = ''.join(nts)
    if kmer in kcount: print(kmer, kcount[kmer])
    else:              print(kmer, 0)
'''