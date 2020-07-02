import display

def discriminant(reduced_form, details):
	a,b,c = reduced_form["a"], reduced_form["b"], reduced_form["c"]
	solution = (b * b) - (4 * a * c)
	if details == True:
		display.explain_disc(a, b, c, solution)
	return solution

def solve_first_degree(reduced_form):
	b,c = reduced_form["b"], reduced_form["c"]
	if b != 0:
		solution = -c / b
		print("The solution is:")
		if solution == 0:
			print(0)
		else:
			print(round(solution, 6))
	else:
		display.error_computing()

def search_interval(start, end, num):
	middle = (start + end) / 2.0
	square_middle = middle * middle
	difference = square_middle - num if square_middle > num else num - square_middle
	if square_middle == num or difference < 0.000001:
		return middle
	elif square_middle < num:
		return search_interval(middle, end, num)
	elif square_middle > num:
		return search_interval(start, middle, num)

def square_root(num):
	if num < 0:
		display.error_negative_root()
	i = 1
	found = False
	result = 0
	while found == False:
		if i * i == num:
			result = i
			found = True
		elif i * i > num:
			result = search_interval(i - 1, i, num)
			found = True
		i += 1
	if result == 0:
		display.error_root()
	return result

def solve_second_degree(reduced_form, discriminant, details):
	a,b,c = reduced_form["a"], reduced_form["b"], reduced_form["c"]
	if discriminant == 0:
		if details == True:
			display.explain_one_solution(a, b)
		print(-b / (2 * a))
	elif discriminant < 0:
		imaginary_part = round(square_root(-discriminant) / (2 * a), 6)
		print(-b / (2 * a)),
		print("- i *"),
		print(imaginary_part)
		print(-b / (2 * a)),
		print("+ i *"),
		print(imaginary_part)
	elif discriminant > 0:
		discriminant_sqrt = square_root(discriminant)
		print(round((-b + discriminant_sqrt) / (2 * a), 6))
		print(round((-b - discriminant_sqrt) / (2 * a), 6))
