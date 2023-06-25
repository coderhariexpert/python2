def get_prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


num = int(input("Enter a number to find its prime factors: "))
prime_factors = get_prime_factors(num)
print("Prime factors of", num, "are:", prime_factors)
