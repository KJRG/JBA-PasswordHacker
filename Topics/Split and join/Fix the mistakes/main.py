text = input()
url_start_sequences = ("https://", "http://", "www.")
words = text.split()
for word in words:
    # finish the code here
    if word.lower().startswith(url_start_sequences):
        print(word)
