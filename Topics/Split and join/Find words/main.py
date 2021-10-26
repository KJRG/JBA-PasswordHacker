words = input().split()
words_ending_with_s = [word for word in words if word.endswith('s')]
result = '_'.join(words_ending_with_s)
print(result)
