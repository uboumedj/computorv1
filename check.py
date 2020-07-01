def is_float(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

def is_valid_variable(string):
	if string == "X^2" or string == "X^1" or string == "X^0" or string == "X":
		return True
	else:
		check_invalid_degree = string.split("^")
		if check_invalid_degree[0] == "X" and len(check_invalid_degree) == 2:
			if is_float(check_invalid_degree[1]):
				print("Polynomial degree: " + check_invalid_degree[1])
				print("The polynomial degree is greater than 2. This program only solves second degree equations.")
				quit()
			else:
				return False
		else:
			return False