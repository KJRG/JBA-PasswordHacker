def fibonacci(n):
    fib_n = 0
    fib_n_plus_1 = 1
    for _ in range(n):
        yield fib_n
        fib_n, fib_n_plus_1 = fib_n_plus_1, fib_n + fib_n_plus_1
