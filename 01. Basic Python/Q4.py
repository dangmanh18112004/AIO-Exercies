def approx_sin(x, n):
	result = 0
	for i in range(n + 1):
		tmp = x ** (2 * i + 1) / compute_factorial(2 * i + 1)
		result += (tmp if i % 2 == 0 else -tmp)
	return result

def approx_cos(x, n):
	result = 0
	for i in range(n + 1):
		tmp = x ** (2 * i) /compute_factorial(2 * i)
		result  += (tmp if i % 2 == 0 else -tmp)
	return result

def approx_sinh(x, n):
	result = 0
	for i in range(n + 1):
		tmp = x ** (2 * i + 1) / compute_factorial(2 * i + 1)
		result += tmp
	return result

def approx_cosh(x, n):
	result = 0
	for i in range(n + 1):
		tmp = x ** (2 * i) / compute_factorial(2 * i)
		result += tmp
	return result

def compute_factorial(n):
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result

if __name__ == '__main__':
	x = float(input("x = "))
	n = int(input("epoch = "))
	print(f"approx sin = {approx_sin(x, n)}")
	print(f"approx cos = {approx_cos(x, n)}")
	print(f"approx sinh = {approx_sinh(x, n)}")
	print(f"approx cosh = {approx_cosh(x, n)}")
