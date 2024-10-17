def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

def generate_blum_numbers(N):
    primes = sieve_of_eratosthenes(N)
    blum_numbers = []
    for p in primes:
        if p % 4 == 3: 
            for q in primes:
                if q % 4 == 3 and p != q: 
                    blum_number = p * q
                    if blum_number < N:
                        blum_numbers.append(blum_number)
    return sorted(set(blum_numbers)) 

def find_blum_pairs(blum_numbers, N):
    blum_pairs = []
    blum_set = set(blum_numbers)
    for i in range(len(blum_numbers)):
        for j in range(i + 1, len(blum_numbers)):
            sum_blum = blum_numbers[i] + blum_numbers[j]
            if sum_blum < N and sum_blum in blum_set:
                blum_pairs.append((blum_numbers[i], blum_numbers[j]))
    return blum_pairs

def check_blum_existence(blum_numbers, M):
    return M in blum_numbers

N = int(input("Nhập số N: "))
M = int(input("Nhập số Blum M cần kiểm tra: "))

blum_numbers = generate_blum_numbers(N)
print("Dãy số Blum nhỏ hơn N:", blum_numbers)

blum_pairs = find_blum_pairs(blum_numbers, N)
print("Các cặp số Blum có tổng cũng là số Blum nhỏ hơn N:", blum_pairs)

exists = check_blum_existence(blum_numbers, M)
if exists:
    print(f"{M}")
else:
    print(f"Số Blum {M} không tồn tại trong dãy số Blum.")
