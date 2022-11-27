def dna(dna):
	dna_replace = {"A":"T", "G":"C"}
	for index in range(len(dna)):
		for i in dna_replace.items():
			if dna[index] in i:
				dna = dna[:index]+i[i.index(dna[index])-1]+dna[index+1:]
			print(dna)
	return dna
print(dna("GTAT"))