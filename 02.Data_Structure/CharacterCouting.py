from collections import Counter

def count_characters1(word):
	dct = {}
	# Count each character in the word
	for c in word:
		if c in dct:
			dct[c] += 1
		else:
			dct[c] = 1
	return dict(sorted(list(dct.items()),key=lambda x : x[0])) # To sort by key

def count_characters2(word): # Using Counter
	return dict(Counter(word))

if __name__ == '__main__':
	word = input("Enter a word: ")
	print(count_characters1(word))
	print(count_characters2(word))