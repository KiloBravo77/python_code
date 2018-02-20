original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first_letter = word[0]
	second_letter = word[1]

	if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u':
		pig_word = word + 'way'
	elif second_letter != 'a' and second_letter != 'e' and second_letter != 'i' and second_letter != 'o' and second_letter != 'u':
		pig_word = word[2:] + first_letter + second_letter + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'

	print(pig_word)
else:
	print("That ain't a work you dummy!")