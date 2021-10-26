# put your python code here
input_numbers = input().split()
number_to_find = input()
number_positions = list()
for i, number in enumerate(input_numbers):
    if number == number_to_find:
        number_positions.append(str(i))
result = " ".join(number_positions) if number_positions else "not found"
print(result)
