def is_isogram(string):
	
	string = string.lower()
	nope = " -"
	
	for x in range(len(string)):
		if (string[x] in string[x+1:len(string)]) and string[x] not in nope:
			return False		
	else:
		return True

