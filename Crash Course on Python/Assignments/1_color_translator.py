# The color_translator function receives the name of a color,
# then prints its hexadecimal value. Currently,
# it only supports the three additive primary colors (red, green, blue),
# so it returns "unknown" for all other colors.

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue"))
print(color_translator("yellow"))
print(color_translator("red"))
print(color_translator("black"))
print(color_translator("green"))
print(color_translator(""))
