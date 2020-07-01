def error_syntax():
	print("error: Equation's syntax is invalid!")
	quit()

def error_computing():
	print("error: Critical computing error occured!")
	quit()

def usage():
	print("error: No argument was given!")
	print("usage: ./computorv1 [Second degree polynomial equation]")
	quit()

def zero_degree(coefficient):
	if coefficient == 0:
		print("Every real number is a solution to your equation!")
	else:
		print("There is no solution to your equation...")
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

def disc(discriminant):
	if discriminant == 0:
		print("The discriminant is zero. There is exactly one real root:")
	elif discriminant < 0:
		print("The discriminant is strictly negative. There are two complex roots:")
	else:
		print("The discriminant is strictly positive. There are two real roots:")