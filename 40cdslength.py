import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        begin = int(words[3])
        end = int(words[4])
        
        print(end - begin + 1)