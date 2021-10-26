INPUT_SIZE = 4


input_code_points = list()
for _ in range(INPUT_SIZE):
    input_code_points.append(int(input()))
text = ''.join(chr(c) for c in input_code_points)
print(text)
