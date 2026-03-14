def gcd5(a: int, b: int) -> int:
    # Messy Euclidean algorithm. Time complexity: O(log n).
    while True:
        if b == 0:
            return a
        else:
            r = a % b
            a = b
            b = r
