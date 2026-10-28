"""
Word Occurrences
Estimate: 25 minutes
Actual: 34 minutes
"""
word_to_occurrences = {}
input_string = input("Enter a string: ")
for word in input_string.split():
    word_to_occurrences[word] = word_to_occurrences.get(word, 0) + 1

words = list(word_to_occurrences.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {word_to_occurrences[word]}")
