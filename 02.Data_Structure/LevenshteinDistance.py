def compute_levenshtein_distance(source, target):
	m = len(source)
	n = len(target)
	# Init matrix levenshtein distance (edit distance)
	matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	# Init cost for 1st row
	for i in range(n + 1):
		matrix[0][i] = i
	# Init cost for 1st column
	for i in range(m + 1):
		matrix[i][0] = i
	# Compute cost
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			sol1 = matrix[i - 1][j] + 1
			sol2 = matrix[i][j - 1] + 1
			sol3 = matrix [i - 1][j - 1] + (0 if target[j - 1] == source[i - 1] else 1)
			matrix[i][j] = min(sol1, sol2, sol3)
	return matrix[-1][-1]
	
	


if __name__ == '__main__':
	source = input("Enter source string: ")
	target = input("Enter target string: ")
	result = compute_levenshtein_distance(source, target)
	print(result)