class pcolors:
	ERROR = "\033[1;91m"
	WARNING = "\033[1;93m"
	VALID = "\033[1;92m"
	BLUE = "\033[1;94m"
	FORMULA = "\033[1;95m"
	STOPCOLOR = "\033[0m"

def error_syntax():
	print(pcolors.ERROR + "error:" + pcolors.STOPCOLOR + " Equation's syntax is invalid!")
	quit()

def error_computing():
	print(pcolors.WARNING + "error:" + pcolors.STOPCOLOR + " Critical computing error occured!")
	quit()

def usage():
	print(pcolors.ERROR + "error:" + pcolors.STOPCOLOR + " No argument was given!")
	print("usage: ./computorv1 [optional flags] [Second degree polynomial equation]")
	print("\nAvailable flags:\n" + pcolors.BLUE + "[-v]" + pcolors.STOPCOLOR + ": explanations on intermediate steps to reach solution")
	quit()

def error_negative_root():
	print(pcolors.WARNING + "error:" + pcolors.STOPCOLOR + " Syntax error while trying to calculate square root: square root of negative number is impossible!")
	quit()

def error_root():
	print(pcolors.WARNING + "error:" + pcolors.STOPCOLOR + " Syntax error while trying to calculate square root!")
	quit()

def error_degree(degree):
	print(pcolors.ERROR + "Polynomial degree: " + str(degree) + pcolors.STOPCOLOR)
	print("The polynomial degree is greater than 2. This program only solves second degree equations!")
	quit()

def error_too_big():
	print(pcolors.WARNING + "error:" + pcolors.STOPCOLOR + " Managing square root of a number that is way too big! Please be more reasonable.")
	quit()

def form(reduced_form):
	a,b,c = reduced_form["a"], reduced_form["b"], reduced_form["c"]
	print("Reduced form:"),
	if a != 0:
		print(a),
		print("* X^2"),
	if b != 0:
		if a != 0:
			if b < 0:
				print("-"),
				b = -b
			else:
				print("+"),
		print(b),
		print("* X^1"),
	if c != 0:
		if a != 0 or b != 0:
			if c < 0:
				print("-"),
				c = -c
			else:
				print("+"),
		print(c),
	if a != 0 or b != 0 or c != 0:
		print("= 0")
	else:
		print("0")

def degree(degree):
	print("Polynomial degree:"),
	print (degree)

def zero_degree(coefficient):
	print("Polynomial degree: 0")
	if coefficient == 0:
		print(pcolors.VALID + "Every real number" + pcolors.STOPCOLOR + " is a solution to your equation!")
	else:
		print("There is " + pcolors.ERROR + "no" + pcolors.STOPCOLOR + " solution to your equation...")
	quit()

def disc(discriminant):
	if discriminant == 0:
		print("The discriminant is zero. There is exactly " + pcolors.BLUE + "one real root:" + pcolors.STOPCOLOR)
	elif discriminant < 0:
		print("The discriminant is strictly negative. There are " + pcolors.WARNING + "two complex roots:" + pcolors.STOPCOLOR)
	else:
		print("The discriminant is strictly positive. There are " + pcolors.BLUE + "two real roots:" + pcolors.STOPCOLOR)

def explain_disc(a, b, c, solution):
	str_a = str(a)
	str_b = str(b)
	str_c = str(c)
	str_sol = str(solution)
	print("The equation's discriminant is calculated with the formula " + pcolors.FORMULA + "[b^2 - 4ac]" + pcolors.STOPCOLOR)
	print("Here, " + pcolors.FORMULA + "[" + str_b + " ^ 2 - 4 * " + str_a + " * " + str_c + " ]" + pcolors.STOPCOLOR + " results in"),
	if solution > 0:
		print(pcolors.VALID),
	elif solution < 0:
		print(pcolors.WARNING),
	elif solution == 0:
		print(pcolors.BLUE),
	print(str_sol + pcolors.STOPCOLOR)

def explain_one_solution(a, b):
	str_a = str(a)
	str_b = str(b)
	print("The solution is obtained with the formula " + pcolors.FORMULA + "[-b / 2a]" + pcolors.STOPCOLOR)
	print("Here, " + pcolors.FORMULA + "[ -" + str_b + " / 2 * " + str_a + " ]" + pcolors.STOPCOLOR + " results in:")

def explain_positive_discriminant(a, b, discriminant):
	str_a = str(a)
	str_b = str(b)
	str_d = str(discriminant)
	print("Solutions are obtained by calculating " + pcolors.FORMULA + "[-b - sqrt(d) / 2a]" + pcolors.STOPCOLOR + " and " + pcolors.FORMULA + "[-b + sqrt(d) / 2a]," + pcolors.STOPCOLOR),
	print("d being the discriminant.")
	print("Here, " + pcolors.FORMULA + "[ -" + str_b + " - sqrt(" + str_d + ") / 2 * " + str_a + " ]" + pcolors.STOPCOLOR + " and "),
	print(pcolors.FORMULA + "[ -" + str_b + " + sqrt(" + str_d + ") / 2 * " + str_a + " ]" + pcolors.STOPCOLOR + " results in:")

def explain_negative_discriminant(a, b, discriminant):
	str_a = str(a)
	str_b = str(b)
	str_d = str(discriminant)
	print("Complex solutions are obtained with " + pcolors.FORMULA + "[(-b / 2a) - i(sqrt(d) / 2a)]" + pcolors.STOPCOLOR + " and " + pcolors.FORMULA + "[(-b / 2a) + i(sqrt(d) / 2a)]," + pcolors.STOPCOLOR),
	print("d being the discriminant and i the imaginary solution of the equation X^2 = -1.")
	print("Here, " + pcolors.FORMULA + "[ -" + str_b + " / 2 * " + str_a + " - i * sqrt(" + str_d + ") / 2 * " + str_a + " ]" + pcolors.STOPCOLOR + " and"),
	print(pcolors.FORMULA + "[ -" + str_b + "/ 2 *" + str_a + "+ i * sqrt(" + str_d + ") / 2 *" + str_a + " ]" + pcolors.STOPCOLOR + " results in:")