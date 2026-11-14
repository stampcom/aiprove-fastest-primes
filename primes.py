import sys

def count_primes(n):
    if n < 2:
        return 0
    size = (n + 1) // 2  # odd numbers only: index i -> value 2i+1
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0  # 1 is not prime
    limit = int(n ** 0.5)
    for v in range(3, limit + 1, 2):
        if sieve[v // 2]:
            start = v * v // 2
            step = v
            sieve[start::step] = b"\x00" * ((size - 1 - start) // step + 1)
    return 1 + sum(sieve)  # +1 for the prime 2

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        print(count_primes(int(data[0])))
