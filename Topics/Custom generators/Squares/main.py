n = int(input())


def squares(count):
    for i in range(1, count + 1):
        yield i ** 2


# Don't forget to print out the first n numbers one by one here
squares_generator = squares(n)
for x in squares_generator:
    print(x)
