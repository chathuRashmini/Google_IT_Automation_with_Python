# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end,
# and returns a list of squares of consecutive numbers
# between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].

def squares(start, end):
	return [x*x for x in range(start, end+1)]

print(squares(2, 3))
print(squares(1, 5))
print(squares(0, 10))
