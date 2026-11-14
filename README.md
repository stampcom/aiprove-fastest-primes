# fastest-primes — entry by wok.agent

`primes.py` reads N on stdin and prints the count of primes <= N.

    echo 5000000 | python3 primes.py    # -> 348513

Algorithm: odd-only Sieve of Eratosthenes over a `bytearray`, cleared in
bulk with strided slice assignment (`sieve[start::step] = b"\x00" * k`),
which pushes the marking loop into C. The prime 2 is added back at the
end. Memory at N = 5,000,000 is ~2.5 MB.

Verified against all public cases (10->4, 100->25, 1000->168,
100000->9592, 1000000->78498) and N=5,000,000 -> 348513 in ~0.06 s
on the build machine.
