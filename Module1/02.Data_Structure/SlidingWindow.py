def slide_window(num_list, k):
	result = []
	for i in range(len(num_list) - k + 1):
		window = num_list[i:i + k]
		max_val = max(window)
		result.append(max_val)
	return result


if __name__ == '__main__':
	num_list = list(map(int, input("num_list = ").split()))
	k = int(input("Enter k: "))
	print(slide_window(num_list, k))
