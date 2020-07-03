import display

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
				display.error_degree(check_invalid_degree[1])
			else:
				return False
		else:
			return False