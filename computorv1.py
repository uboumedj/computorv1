import sys
import check
import display
import calculate

def parse_one_side(side, coefficients, sign):
	i = 0
	minus = 1
	while i < len(side):
		if check.is_float(side[i]):
			value = float(side[i])
			if i + 1 < len(side):
				if side[i + 1] == "+" or side[i + 1] == "-":
					coefficients["c"] += value * sign * minus
				elif side[i + 1] == "*":
					if i + 2 < len(side) and check.is_valid_variable(side[i + 2]):
						if side[i + 2] == "X^2":
							coefficients["a"] += value * sign * minus
						elif side[i + 2] == "X^1" or side[i + 2] == "X":
							coefficients["b"] += value * sign * minus
						else:
							coefficients["c"] += value * sign * minus
						i += 2
					else:
						display.error_syntax()
				else:
					display.error_syntax()
			else:
				coefficients["c"] += value * sign * minus
			minus = 1
		elif side[i] == "+" or side[i] == "-":
			if i + 1 < len(side):
				minus = -1 if side[i] == "-" else 1
			else:
				display.error_syntax()
		elif check.is_valid_variable(side[i]):
			if side[i] == "X^2":
				coefficients["a"] += 1 * sign * minus
			elif side[i] == "X^1" or side[i] == "X":
				coefficients["b"] += 1 * sign * minus
			else:
				coefficients["c"] += 1 * sign * minus
		else:
			display.error_syntax()
		i += 1
	return coefficients

def get_coefficients(equation):
	coefficients = {
		"a": 0,
		"b": 0,
		"c": 0
	}
	left_side = equation[0].split()
	right_side = equation[1].split()
	coefficients = parse_one_side(left_side, coefficients, 1)
	coefficients = parse_one_side(right_side, coefficients, -1)
	return coefficients

def parse_equation(input):
	equation = input.split('=')
	if len(equation) != 2:
		display.error_syntax()
	else:
		coefficients = get_coefficients(equation)
	return coefficients

def parse_degree(reduced_form):
	if reduced_form["a"] != 0:
		return 2
	elif reduced_form["b"] != 0:
		return 1
	else:
		display.zero_degree(reduced_form["c"])

def main(argv):
	if len(argv) <= 1:
		display.usage()
	else:
		if argv[1] != "-v":
			reduced_form = parse_equation(argv[1])
			details = False
		else:
			reduced_form = parse_equation(argv[2])
			details = True
		display.form(reduced_form)
		degree = parse_degree(reduced_form)
		display.degree(degree)
		if degree == 2:
			discriminant = calculate.discriminant(reduced_form, details)
			display.disc(discriminant)
			calculate.solve_second_degree(reduced_form, discriminant, details)
		else:
			calculate.solve_first_degree(reduced_form)

if __name__ == "__main__":
	main(sys.argv)