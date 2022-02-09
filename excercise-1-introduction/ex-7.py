# You are given the following DNA sequence:
# AAACGCTGTCAATACAATCTTYCTAGATATTCGGATTTGAATTTTGCAAAA
# write a loop that will split the above sequence in triplets
# and print them?

dna = 'AAACGCTGTCAATACAATCTTYCTAGATATTCGGATTTGAATTTTGCAAAA'
splitted = []

while dna:
    splitted.append(dna[:3])
    dna = dna[3:]

print(splitted)