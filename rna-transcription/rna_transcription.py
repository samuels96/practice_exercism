import string

def to_rna(dna_strand):
	
	dna = "GCTA"		
	rna = ""
	
	for x in dna_strand:
		if x not in dna:
			raise Exception("\nWrong input entered \nEnter RNA - G,C,T,A")
		if x == "G":
			rna += "C"
		if x == "C":
			rna += "G"
		if x == "T":
			rna += "A"
		if x == "A":
			rna += "U"
	return rna

print (to_rna("SDSDSA"))
	
