# Word Count

import re

text = input("Enter a text paragrah: ")

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count:")

for word, count in sorted(word_count.items()):
    print(word, ":", count)


