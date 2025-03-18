import sys
import gzip

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('#'): continue # there is also str.endswith()
        f = line.split()
        feature = f[2]
        if feature not in count: count[feature] = 0
        count[feature] += 1

for k in sorted(count): print(k, count[k])    # sort by value    
 
#for f, n in count.items(): print(f, n)
     
 
# for k, v in sorted(count.items(), key = lambda item:item[1]): # sort by key not value
    # print(k, v)

def by_value(tuple):
    return tuple[1]
    
for k, v in sorted(count.items(), key = by_value):
    print(k, v)