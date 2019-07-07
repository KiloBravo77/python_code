def swap_case(s):
	#charList = list(s)
	#newstring = ""

	#for item in charList:
	#	if item.isupper():
	#		newstring += item.lower()
	#	else:
	#		newstring += item.upper()

	return s.swapcase() #newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)