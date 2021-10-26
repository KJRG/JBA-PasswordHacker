word_1 = input()
word_2 = input()

result = ''.join((letter_1 + letter_2 for (letter_1, letter_2) in zip(word_1, word_2)))
print(result)
