

animal_sounds = {'dog': 'woof', 'cat':'meow'}
print(animal_sounds)
print(animal_sounds['cat'])

animal_sounds['pig'] = 'oink'
print(animal_sounds)

animal_sounds['cat'] = 'mew'
print(animal_sounds)

del animal_sounds['cat']
print(animal_sounds)

if 'dog' in animal_sounds: print(animal_sounds['dog'])

for key in animal_sounds: print(f'{key} goes {animal_sounds[key]}')

for k, v in animal_sounds.items(): print(f'{k} goes {v}')

print(animal_sounds.keys(), animal_sounds.values(), list(animal_sounds.values()))

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
    
print(kd_dict('VEDANAYAK'))

seq = 'ATGCATGCGAGATATAGAGATAGAAAAAAAAAGGATAA'

count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
print(count)

















'''
import argparse # gives you a unit standard front end
                # do -- for optional addons
                # make unix software people would want to use
import sys

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'file name')
parser.add_argument('--window', type = int, default = 11)
parser.add_argument('--threshold', type = float, default = 1.1)
parser.add_argument('--lowercase', action = 'store_true')

sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'file name')
parser.add_argument('--minchar', type = int, default = 29)
help = 'min line length [%(default)i]'
arg = parser.parse_args()

with open(arg.file) as fp:
    for line in fp:
        if len(line) >= arg.minchar:print(len(line))

sys.exit()

# python3 50demo.py ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz  | sort -nk2 | less

import random

import mcb185

k = 4
kmer2count = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in kmer2count: kmer2count[kmer] = 0
        kmer2count[kmer] += 1

for kmer, n in kmer2count.items():
    print(kmer, n)



names = []
vals = []
name2val = {}

with open(sys.argv[1]) as fp:
    for line in fp:
        name, val = line.split()
        f = line.split()
        name2val[name] = val
        
        names.append(name)
        vals.append(val)

#for key in name2val:
#    print(key, name2val[key])

names = list(name2val.keys())

for i in range(10):
    token = random.choice(names)
    print(token, name2val[token])


for i in range(100000):
    name = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k = 9)
    name = ''.join(name)
    value = random.random()
    print(name, value)
'''