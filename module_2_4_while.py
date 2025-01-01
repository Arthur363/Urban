numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
while i < len(numbers):
    num = numbers[i]
    if num > 1:
        j = 2
        is_prime = True
        while j < num:
            if (num % j) == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
    i += 1
print("Primes:", primes)
print("Not Primes:", not_primes)