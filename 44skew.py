import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10


for i in range(len(seq) - w + 1): 

    if i == 0:
        window = seq[i:i+w]
        g = window.count('G')
        c = window.count('C')
    
    else: 
        on = seq[i + w - 1]
        off = seq[i - 1]
        
        if on == 'G': g += 1
        elif on == 'C': c += 1
        elif off == 'G': g -= 1
        elif off == 'C': c -= 1

    comp = (g + c) / len(seq)
    skew = (g - c) / (g + c)
    
    print(i, comp, skew)
        