triangle_height = int(input())
last_line_length = 2 * triangle_height - 1
for i in range(0, triangle_height):
    chars_in_line = 2 * i + 1
    line = ('#' * chars_in_line).center(last_line_length)
    print(line)
