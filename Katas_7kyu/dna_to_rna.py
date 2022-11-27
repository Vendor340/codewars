
def dna_to_rna(dna):
	return dna.translate(dna.maketrans("GCAT", "GCAU"))
print(dna_to_rna("TTTT"))