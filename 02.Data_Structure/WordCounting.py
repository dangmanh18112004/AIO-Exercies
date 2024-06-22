path = 'P1_data.txt'
bag_words = {}
# Cach trau bo
with open(path) as fi:
	document = fi.read()
	words = document.lower().split()
	for w in words:
		if w in  bag_words:
			bag_words[w] += 1
		else:
			bag_words[w] = 1
print(dict(sorted(list(bag_words.items()), key=lambda x : x[0])))