import streamlit as st

file_path = 'vocab.txt'
def load_vocabs(file_path):
	with open(file_path) as fi:
		lines = fi.readlines()
	words = sorted(set([line.strip().lower() for line in lines]))
	return words

def calc_levenshtein_distance(token1, token2):
	num_row = len(token1)
	num_col = len(token2)
	d = [[0 for _ in range(num_col + 1)] for _ in range(num_row + 1)]

	# Init the distance
	for i in range(num_col + 1):
		d[0][i] = i

	for i in range(num_row + 1):
		d[i][0] = i

	for i in range(1, num_row + 1):
		for j in range(1, num_col + 1):
			del_cost = d[i - 1][j] + 1
			ins_cost = d[i][j - 1] + 1
			sub_cost = d[i - 1][j - 1] + (0 if token1[i - 1] == token2[j - 1] else 1)
			d[i][j] = min(del_cost, ins_cost, sub_cost)
	
	return d[-1][-1]

if __name__ == '__main__':
	st.title("Word Correction using Levensthein Distance")
	word = st.text_input("Word: ")
	vocabs = load_vocabs(file_path)

	if st.button("Compute"):
		# Compute Levensthein Distance
		leven_distances = dict()
		for vocab in vocabs:
			leven_distances[vocab] = calc_levenshtein_distance(word, vocab)

		# Sorted by distance
		sorted_distances = dict(sorted(leven_distances.items(), key=lambda x: x[1]))
		correct_word = list(sorted_distances.keys())[0]
		st.write("Correct word: ", correct_word)

		col1, col2 = st.columns(2)
		col1.write("Vocabulary:")
		col1.write(vocabs)

		col2.write("Distances:")
		col2.write(sorted_distances)

		