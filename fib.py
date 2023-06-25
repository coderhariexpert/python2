def generate_fibonacci(n):
    fibonacci = [0, 1]

    while len(fibonacci) < n:
        next_number = sum(fibonacci[-2:])
        fibonacci.append(next_number)

    return fibonacci


count = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_series = generate_fibonacci(count)
print("Fibonacci Series:", fibonacci_series)

