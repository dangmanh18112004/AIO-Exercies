import math

def is_number(x):
	try:
		float(x)
	except:
		return False
	return True

def is_valid_activation_name(act_name):
	return act_name in ['relu', 'sigmoid', 'elu']

def calc_sigmoid(x):
	result = 1 / (1 + math.exp(-x))
	return result

def calc_relu(x):
	return x if x > 0 else 0

def calc_elu(x):
	alpha = 0.01
	return alpha * (math.exp(x) - 1) if x <= 0 else x

if __name__ == '__main__':
	x = input("Input x = ")
	if is_number(x):
		x = float(x) # Convert x to float
		act_name = input("Input activation Function (sigmoid|relu|elu): ").lower()
		if is_valid_activation_name(act_name):
			result = 0
			if act_name == 'sigmoid':
				result = calc_sigmoid(x)
			elif act_name == 'relu':
				result = calc_relu(x)
			else:
				result = calc_elu(x)
			print(f'{act_name}: f({x}) = {result}')
		else:
			print(f"{act_name} is not supported")
	else:
		print("x must be a number")