def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    return list(filter(lambda c: c in vowels, letters))
