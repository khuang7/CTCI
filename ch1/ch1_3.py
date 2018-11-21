

def main():
	string = "  a very long string with multiple spaces  "
	string = string.strip()

	print ("String is now" , string)

	string = string.replace(" ", "%20")
	print (string)

main()