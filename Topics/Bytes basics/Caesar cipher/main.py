def encrypt(text):
    return ''.join(chr(ord(c) + 1) for c in text)


input_text = input()
print(encrypt(input_text))
