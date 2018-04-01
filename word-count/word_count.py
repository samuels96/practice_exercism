import string
def word_count(phrase):
	
	#Replace everything else than letters or quotation marks by space 
	for x in phrase:
		if x != "'"  and x not in (string.ascii_letters) and x not in (string.digits):
			phrase = phrase.replace(x, " ")
			
	#Turn phrase into list
	phrase = phrase.lower().split()
	
	#Exclude quotation marks that do not serve as apostrophe
	newlst = []
	for x in phrase:
		if x.startswith("'") == True:
			x = x.replace("'","")
			newlst.append(x)
		else:
			newlst.append(x)
	
	#Turns newlst into dictionary with word count as a value		
	phrase_dic = (set(newlst)) 
	result =  {}
	for x in phrase_dic:
		result.update({x: newlst.count(x)})
	
	return result

