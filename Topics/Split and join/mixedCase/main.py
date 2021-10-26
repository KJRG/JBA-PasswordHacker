words = input().split()
result = words[0]
if len(words) > 1:
    capitalized_part = "".join([word.capitalize() for word in words[1:]])
    result = f"{words[0]}{capitalized_part}"
print(result)
