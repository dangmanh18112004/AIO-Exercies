def is_integer(n):
	return n.isnumeric()

def is_greater_zero(tp, fp, fn):
	return tp > 0 and fp > 0 and fn > 0

def calc_precision(tp, fp):
	return tp / (tp + fp)

def calc_recall(tp, fn):
	return tp / (tp + fn)

def calc_f1_score(tp, fp, fn):
	precision = calc_precision(tp, fp)
	recall = calc_recall(tp, fn)
	return 2 * precision * recall / (precision + recall)

if __name__ == '__main__':
	tp, fp, fn = input().split()
	# Check integer
	if is_integer(tp):
		tp = int(tp)
	else:
		print("tp must be int")
		quit()
	
	if is_integer(fp):
		fp = int(fp)
	else:
		print("fp must be int")
		quit()
	
	if is_integer(fn):
		fn = int(fn)
	else:
		print("fn must be int")
		quit()
	
	# Check greater than zero
	if is_greater_zero(tp, fp, fn):
		precision = calc_precision(tp, fp)
		recall = calc_recall(tp, fn)
		f1_score = calc_f1_score(tp, fp, fn)
		print(f"precision is {precision}")
		print(f"recall is {recall}")
		print(f"f1-score is {f1_score}")
	else:
		print("tp and fp and fn must be greater than zero")
		