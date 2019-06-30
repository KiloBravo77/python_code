from collections import Counter

word_list = []

for _ in range(int(input())):
	word = input()
	word_list.append(word)

word_dict = Counter(word_list).values()
word_counts = ""

for value in word_dict:
	word_counts = word_counts + " " + str(value)

print(len(Counter(word_list).keys()))
print(word_counts[1:])