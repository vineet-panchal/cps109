# def is_prime(n):
#     if n < 1:
#         return False
#     elif n == 2:
#         return True
#     else:
        
#         for i in range(2, n):
#             if n % i != 0:
#                 return 
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# def is_prime(n):
#     count = 2
#     if n % count != 0:
#         if count >= n - 2:
#             return True
#         count += 1
#         is_prime(n)
        
#     else:
#         return False

# def is_prime(n):
#     if n < 1:
#         return False
#     count = 0
#     difference = 0
#     for i in range(2, n):
#         difference += 1
#         if n % i != 0:
#             count += 1
#         if count == difference:
#             return True
#         return False

if __name__ == "__main__":
    print(get_primes(1, 100))