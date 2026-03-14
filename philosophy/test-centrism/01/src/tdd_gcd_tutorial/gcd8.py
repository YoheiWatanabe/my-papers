def gcd8(a: int, b: int) -> int:
    # Naive division search (brute-force). Time complexity: O(n).
    m = min(a, b)
    for i in range(m, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
