def is_valid_char(char):
	return char.isalnum() or char == '\''

def index_first_vowel(word):
	for i in range(len(word)):
		if word[i].lower() in ('a', 'e', 'i', 'o', 'u'):
			return i;
	return -1

def translate_word(word):
	is_upper = word[0].isupper()
	idx = index_first_vowel(word)
	ret = ""
	if idx < 1:
		ret = word + "yay"
	else:
		ret = word[idx:] + word[:idx] + "ay"
	if is_upper:
		return ret.capitalize()
	return ret
	
def translate(words):
	curr_word = ""
	text_piglatin = ""
	for i in range(len(words)):
		char = words[i]
		if is_valid_char(char):
			curr_word += char
		else:
			if curr_word:
				text_piglatin += translate_word(curr_word)
				curr_word = ""
			text_piglatin += char
	
	if curr_word:
		text_piglatin += translate_word(curr_word)

	return text_piglatin
