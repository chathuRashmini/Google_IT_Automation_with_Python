# The highlight_word function changes the given word in a sentence to 
# its upper-case version. For example, highlight_word("Have a nice day", "nice")
# returns "Have a NICE day".

def highlight_word(sentence, word):
	newsentence = ""

	sentence = sentence.split()
	index = sentence.index(word)
	sentence[index] = word.upper()

	for w in sentence:
		newsentence += w + " "
	return(newsentence)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud !", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
