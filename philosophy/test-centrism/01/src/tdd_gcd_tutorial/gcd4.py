def gcd4(a: int, b: int) -> int:
    # Divide the larger number by the smaller one. If there is a remainder, return the remainder; if it divides evenly, return the smaller number.
    x = max(a, b)
    y = min(a, b)
    r = x % y
    if r:
        y = r
    return y
