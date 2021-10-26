words = input().split("_")
result = "".join((word.capitalize() for word in words))
print(result)
