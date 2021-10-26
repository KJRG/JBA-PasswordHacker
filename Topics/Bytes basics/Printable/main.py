PRINTABLE_RANGE_START = 32
PRINTABLE_RANGE_END = 126


def is_printable(code_point):
    return PRINTABLE_RANGE_START <= code_point <= PRINTABLE_RANGE_END


input_code_point = int(input())
if is_printable(input_code_point):
    print(chr(input_code_point))
else:
    print("False")
