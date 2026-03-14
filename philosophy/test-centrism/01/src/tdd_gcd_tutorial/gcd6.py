def gcd6(a: int, b: int) -> int:
    # Overly short Euclidean algorithm. Time complexity: O(log n).
    return a if b == 0 else gcd6(b, a % b)
