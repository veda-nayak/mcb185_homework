gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "o" | grep "n" | grep "r" | grep "c" | grep "a" | grep "z" | grep "i" | grep -v sort
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep 

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep "[zoniacr]{3,}"


gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "[zoniacr]{0,}+r+[zoniacr]{0,}" | grep -Ev "[bcdefghjklmpqstuvwxy]"
# output = 24

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "[zoniacr]{4,}" | grep -Ev "[bcdefghjklmpqstuvwxy]"
# output 19


# 4 letters long
# must contain r
# cannot contain any other letters other than the 7