# Returns how many digits the number has.
# For example: 25 has 2 digits and 144 has 3 digits. 

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n>0):
		count += 1
		n = int(n/10)
	return count

print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))
