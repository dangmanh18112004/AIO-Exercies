import math
import random 

def is_integer_number(n):
	return n.isnumeric() # If n is a (string | negative integer | float) then return False

def calc_MAE(n, predict, target):
	result = 0
	for i in range(n):
		result += abs(predict[i] - target[i])
	result /= n
	return result

def calc_MSE(n, predict, target):
	result = 0
	for i in range(n):
		result += (predict[i] - target[i]) ** 2
	result /= n
	return result

def calc_RMSE(n, predict, target):
	result = math.sqrt(calc_MSE(n, predict, target))
	return result

if __name__ == '__main__':
	n = input("Input number of samples (integer number) which are generated: ")
	if is_integer_number(n):
		n = int(n) # Convert n to integer
		# Random predict & target value
		loss_name = input("Input loss name: ")
		# Generate 2 lists to store pred value & target value
		pred_list = []
		target_list = []
		for i in range(n):
			pred = random.uniform(0, 10)
			pred_list.append(pred)
			target = random.uniform(0, 10)
			target_list.append(target)
			loss = 0
			if loss_name == 'MAE':
				loss = abs(pred - target)
			else:
				loss = (pred - target) ** 2
			print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')
		cost = 0
		if loss_name == 'MAE':
			cost = calc_MAE(n, pred_list, target_list)
		elif loss_name == 'MSE':
			cost = calc_MSE(n, pred_list, target_list)
		else:
			cost = calc_RMSE(n, pred_list, target_list)
		print(f"final {loss_name}: {cost}")
	else:
		print("number of samples must be an integer number")
