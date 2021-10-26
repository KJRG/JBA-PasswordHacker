input_number = int(input())
number_as_bytes = input_number.to_bytes(2, 'little')
sum_of_bytes = sum(number_as_bytes)
print(sum_of_bytes)
