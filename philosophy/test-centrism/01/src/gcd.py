def gcd1(a: int, b: int) -> int:
    return b

def gcd2(a: int, b: int) -> int:
    return min(a, b)

def gcd3(a: int, b: int) -> int:
    x = max(a, b)
    y = min(a, b)
    r = x % y
    if r:
        y = r
    return y

def gcd4(a: int, b: int) -> int:
    m = min(a, b)
    for i in range(m, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def gcd5(a: int, b: int) -> int:
    while True:
        if b == 0:
            return a
        else:
            r = a % b
            a = b
            b = r

def gcd6(a: int, b: int) -> int:
    return a if b == 0 else gcd6(b, a % b)

def gcd7(a: int, b: int) -> int:
    while b !=0 :
        a, b = b, a % b
    return a