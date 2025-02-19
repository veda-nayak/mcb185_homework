'''
=	assignment	    s = 'hello'
+	concatenation	s = 'hello' + 'world'
*	repetition	    polyA = 'A' * 100
>	comparison	    if s1 < s2
<	comparison	    if s1 > s2
==	comparison	    if s1 == s2

len(s)	get the length of a string
chr(n)	get the character whose ASCII value is n
ord(c)	get the ASCII value of the character c

s.count(s1)	        # number of occurrences of s1 in s
s.endswith(s1)	    # True if s ends with s1 ex. if s ends with .gz --> gzipped
s.startswith(s1)	# True if s starts with s1
s.upper()	        # uppercase version of s
s.lower()	        # lowercase version of s
s.rstrip()	        # strip characters from the right (spaces by default)
s.replace(a, b)	    # convert substring a to b 
                        (WON'T CHANGE S ITSELF, 
                        MAKES A COPY OF S AND CHAGES THE COPY)

if 'WORD' in string: do __
                       
list.append(i)              # add something to the end of a list
list.pop()                  # get the last value from a list
list.sort()                 # sort a list
list.sort(reverse = True)   # sort backwards

string = ''.join(list)      # list -> string, '-' adds a hyphen in 
                              between list[i]'s
line = line.splut(',')      # split string at the "," for CSV and
                              \t for TSV
                                                          
import sys
print(sys.argv) # argument, if you do sys.argv[0] it takes the first argument
                              

'''



'''
seq = 'GAATTC'
print(seq[0], seq[4])
print(seq[-1]) # counts backwards


for nt in seq:  # this is better
    print(nt, end = '')
print()

s = 'ABCDEFGHIJ'
print(s[0:5])

histogram = (0.5, 0.4, 0.3, 0.2, 0.1)
for p in histogram:
    print(p)
    
# provide you a tuple containing the 
# index and value in separate named variables

for i in range(len(seq)):
    print(i, seq[i])
    

# OR

for i ,p in enumerate(histogram): 
    print(i, p)
    
    
# You can't change the contents of a tupple but you can for a List
histogram = [0.5, 0.4, 0.3, 0.2, 0.1]


container = []
for i in range(50):
    container.append(i)
print(container)

# remove elements from the end of the list
last = container.pop()
print(last)


s = 'GAATTC'
container = []

for nt in s:
    container.append(nt)
print(container)



import random

seq = []

for i in range(1000000000):
    nt = random.choice('ATGC')
    seq.append(nt)
    

dna = ''.join(seq)

if 'GAATTCATAGCAGGG' in dna: print('found')

print(dna)



import sys

def tm(s):
    a = s.count('A')
    c = s.count('C')
    t = s.count('T')
    g = s.count('G') 
    return (a+t)*2 + (g+c)*4    

for oligo in sys.argv[1:]:
    print(oligo, tm(oligo))
    


def list_mean(l):
    total = 0
    list_sum = 0
    for num in l:
        list_sum += num
        total += 1
    return list_sum / total

l = [1, 2, 3]
print(list_mean(l))


def minimum(l):
   new_l = l.sort(l, reverse = True)
   return new_l[0]

l = [2,3,7,1,5]
minimum(l)

'''

import random
things_tupple = ('socks', 'pants', 'shirt', 'hat', 'gloves') # this is a tupple
    # We can't add tings to this

things = ['socks', 'pants', 'shirt', 'hat', 'gloves']
print(things)
things.append('scarf')
print(things)

# index
print(things[0])
print(things[0:2]) # works just like the range operator, prints 0 and 1, not 2
print(things[0:4:2]) # 0 - 4 by 2's
print(things[4:0:-2]) # start at 4, go back by 2's
print(things[2:]) # start at 2, go to the end
print(things[::-1]) # how to reverse a list

print(things[0][1]) # socks --> o



