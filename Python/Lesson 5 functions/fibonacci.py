def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

num_terms = int(input("Enter the number of terms: "))
fib_result = fibonacci(num_terms)
print(f"The Fibonacci series is: {fib_result}")
