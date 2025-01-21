 gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E "^[zoniacr]*r[zoniacr]*r*[zoniacr]*$" | grep -E ".{4,}" 
