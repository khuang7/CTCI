

var = "heyaa"
array = []

def main():
	for char in var:
		print ("looking at", char)
		if char in array:
			print ("FALSE")
			return False
		else:
			print("adding here")
			array.append(char)

	print("TRUE")
	return True
	
main()
