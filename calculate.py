def discriminant(reduced_form):
	a,b,c = reduced_form["a"], reduced_form["b"], reduced_form["c"]
	return (b * b) - (4 * a * c)

def solve_first_degree(reduced_form):
	b,c = reduced_form["b"], reduced_form["c"]
	if b != 0:
		solution = -c / b
		print("The solution is:")
		if solution == 0:
			print(0)
		else:
			print(solution)
	else:
		display.error_computing()

def solve_second_degree(reduced_form, discriminant):
	a,b,c = reduced_form["a"], reduced_form["b"], reduced_form["c"]
	if discriminant == 0:
		print(-b / (2 * a))