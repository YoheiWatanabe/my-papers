def gcd7(a: int, b: int) -> int:
    # Human-readable Euclidean algorithm. Time complexity: O(log n).
    while b !=0 :
        a, b = b, a % b
    return a
