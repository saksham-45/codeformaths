import time
from typing import List


def sieve(n: int) -> List[int]:
    """Return list of primes up to n (inclusive) using an efficient sieve."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"  # 0 and 1 are not primes
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n+1:step] = b"\x00" * ((n - start) // step + 1)
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    n = 100
    t0 = time.time()
    primes = sieve(n)
    t1 = time.time()
    print(f"Primes up to {n}: {primes}")
    print(f"Found {len(primes)} primes in {t1 - t0:.6f}s")
