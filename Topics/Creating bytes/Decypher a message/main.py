def sum_of_bytes(number):
    return sum(number.to_bytes(2, 'little'))


def decode(msg, offset):
    return ''.join(chr(ord(c) + offset) for c in msg)


encoded_msg = input()
key = int(input())
decoded_msg = decode(encoded_msg, sum_of_bytes(key))
print(decoded_msg)
