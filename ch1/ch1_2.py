var1 = "heyaa"
var2 = ""


def main():
	sort_var1 = sortList(var1)
	sort_var2 = sortList(var2)

	if sort_var1 == sort_var2:
		print("TRUE")
	else:
		print("FALSE")


def sortList(str):
	b = sorted(str)
	c = ''.join(b)
	return c

main()
