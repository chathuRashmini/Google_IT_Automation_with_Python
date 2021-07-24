# This function receives the first_name and last_name parameters and 
# then returns a properly formatted string last name first and first name secondly.
# Ex:
# function -> print(format_name("Ella", "Fitzgerald"))
# output -> Name: Fitzgerald, Ella
#
# If only one name parameter is supplied;
# function -> print(format_name("Adele", ""))
# output -> Name: Adele
#
# function -> print(format_name("", "Einstein"))
# output -> Name: Einstein


def format_name(first_name, last_name):
	# code goes here
	if len(first_name) ==0 and len(last_name) == 0 :
		return ""
	elif len(last_name) == 0 :
		string = first_name
	elif len(first_name) == 0 :
		string = last_name
	else:
		string = last_name + ", " + first_name

	return string

print(format_name("Ernest", "Hemingway"))

print(format_name("", "Madonna"))

print(format_name("Voltaire", ""))

print(format_name("", ""))
