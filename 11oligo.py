def tm(a, c, g, t):
    length = a + c + g + t
    if length <= 13: 
        temp = (a + t)*2 + (g + c)*4
        oligo = "short"
    else:
        temp = 64.9 + (41*(g + c - 16.4) / length)
        oligo = "long"
    print("Your oligo is", oligo, "with a Tm of", temp, "degrees")
    return temp

tm(2, 2, 2, 2)
tm(4, 4, 4, 4)
