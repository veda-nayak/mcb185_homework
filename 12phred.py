
# 0.001 = 1 x 10^-3 = 1e-3 = 1 * 10 ** -3

import math

def prob_to_char(p):
    
    pqv =  - int(math.log10(p) * 10) # phred quality value
    symbol = chr(pqv + 33)
    print("A probability of", p, "has a symbol of", symbol) 
    

prob_to_char(1e-3)


def char_to_p(c):
    pqv = ord(c) - 33
    prob = 10 ** (-pqv/10)
    print("A symbol of", c, "has a probability of", prob) 

char_to_p('A')
