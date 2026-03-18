def gcd4(a: int, b: int) -> int:
    # One step of the Euclidean algorithm.
    # Replace the smaller number with the remainder.
    a, b = max(a, b), min(a, b)
    return a % b if a % b else b

# def gcd4(a: int, b: int) -> int:
    # One step of the Euclidean algorithm.
    # Replace the smaller number with the remainder.
#     x = max(a, b)
#     y = min(a, b)
#     r = x % y
#     if r:
#         y = r
#     return y