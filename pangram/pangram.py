import string

def is_pangram(sentence):
    letters = string.ascii_lowercase
    sentence = sentence.lower()
    for x in letters:
        if x not in sentence:
            return False
    return True
