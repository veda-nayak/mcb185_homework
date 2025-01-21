
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "[aeiou][aeiou][aeiou][aeiou]" | wc -l
gunzip -c dictionary.gz | grep "[qwrtypsdfghjklzxcvbnm][qwrtypsdfghjklzxcvbnm][qwrtypsdfghjklzxcvbnm][qwrtypsdfghjklzxcvbnm][qwrtypsdfghjklzxcvbnm]" | wc -l


# part 2
gunzip -c MCB185/data/jaspar2024_core.transfac.gz | grep "tax_group" | wc
# output = 2346
