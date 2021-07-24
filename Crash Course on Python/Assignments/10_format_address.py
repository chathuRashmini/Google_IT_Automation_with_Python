# The format_address function separates out parts of the address string 
# into new strings: house_number and street_name, and returns:
# "house number X on street named Y".
# The format of the input string is: numeric house number, followed by the street
# name which may contain numbers, but never by themselves,
# and could be several words long.
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".

def format_address(address_string):
  street_name = ""
  addressArray = address_string.split()
  house_number = addressArray[0]
  for x in range(1, len(addressArray)):
    street_name += addressArray[x] + " "

  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))

print(format_address("1001 1st Ave"))

print(format_address("55 North Center Drive"))
