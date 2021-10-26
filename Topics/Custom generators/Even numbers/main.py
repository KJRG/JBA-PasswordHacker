n = int(input())


def even():
    i = 0
    while True:
        yield i
        i += 2


# Don't forget to print out the first n numbers one by one here
even_number_gen = even()
for _ in range(n):
    print(next(even_number_gen))
