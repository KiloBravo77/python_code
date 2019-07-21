import textwrap

def wrap(string, max_width):
	wrapped_word = ""
	for word in textwrap.wrap(string, max_width):
		#print(word)
		wrapped_word += word + "\n"
	return wrapped_word

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)