def to_rna(dna_strand):
	dna_strand = dna_strand.upper()
	for x in dna_strand:
		if x == "G":
			x = "C"
		if x == "C":
			x = "G"
		if x == "T":
			x = "A"
		if x == "A":
			x = "U"
	return dna_strand
	
print (to_rna("GCTA"))
