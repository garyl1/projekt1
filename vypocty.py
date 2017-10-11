def series_sum(n):
    mezisoucet = 0
    x = 1
    for i in range(n):
         mezisoucet = mezisoucet + x
         x = x + 1
    return mezisoucet

# print(series_sum(1))     # 1
# print(series_sum(5))     # 15
# print(series_sum(10))    # 55


def factorial(n):
    mezisoucin = 1
    x = 0
    while x < n:
        x = x + 1
        mezisoucin = mezisoucin * x
    return mezisoucin

# print(factorial(0))      # 1
# print(factorial(1))      # 1
# print(factorial(10))     # 3628800
# print(factorial(50))


def digit_sum(n):
    cislo = n
    mezisoucet = 0
    while cislo > 0:
        zbytek = cislo % 10
        cislo = cislo // 10
        mezisoucet += zbytek

    return mezisoucet


# print(digit_sum(0))              # 0
# print(digit_sum(274))            # 13
# print(digit_sum(123456789))      # 45


def divisors(n):
    for potdelitele in range(1, n+1):
        if n % potdelitele == 0:
            print(potdelitele)


# divisors(1)     # 1
# divisors(5)     # 1 5
# divisors(42)    # 1 2 3 6 7 14 21 42
# divisors(127)   # 1 127
# divisors(1024)  # 1 2 4 8 16 32 64 128 256 512 1024


def divisors_count(n):
    vysledek = 0
    for potdelitele in range(1, n+1):
        if n % potdelitele == 0:
            vysledek += 1

    return vysledek


# print(divisors_count(1))     # 1
# print(divisors_count(5))     # 2
# print(divisors_count(42))    # 8
# print(divisors_count(127))   # 2
# print(divisors_count(1024))  # 11

def is_prime(n):
    return divisors_count(n) == 2

# print(is_prime(1))      # False
# print(is_prime(2))      # True
# print(is_prime(3))      # True
# print(is_prime(42))     # False
# print(is_prime(127))    # True


def primes_less_than(limit):
    for cislo in range(limit):
        if is_prime(cislo):
            print(cislo)

primes_less_than(5)      # 2 3
primes_less_than(15)     # 2 3 5 7 11 13
primes_less_than(100)
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97