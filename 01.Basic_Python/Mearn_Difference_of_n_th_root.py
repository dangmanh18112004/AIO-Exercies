def calc_MD_nRE(y, y_hat, n, p):
	result = (y ** (1/n) - y_hat ** (1/n)) ** p
	return result

if __name__ == '__main__':
	y = float(input('y = '))
	y_hat = float(input('y_hat = '))
	n = int(input("Root = "))
	p = int(input("Degree = "))
	print(f"Loss = {calc_MD_nRE(y, y_hat, n, p)}")