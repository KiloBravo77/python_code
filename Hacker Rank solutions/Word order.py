from collections import Counter

word_list = []

for _ in range(int(input())):
	word = input()
	word_list.append(word)

print(len(Counter(word_list).keys()))
print(*Counter(word_list).values())