import string
lower = [x for x in string.ascii_lowercase]
upper = string.ascii_uppercase

def hey(phrase):
	phrase = phrase.replace(" ","")
	if phrase.endswith("?") and phrase.isupper():
		return ("Calm down, I know what I'm doing!")
	if phrase.endswith("?"):
		return ("Sure.")
	if phrase.isupper() and phrase.endswith("?") == False:
		return ("Whoa, chill out!")
	if len(phrase) == 0 or "\t" in phrase:
		return ("Fine. Be that way!")
	else:
		return ("Whatever.")
