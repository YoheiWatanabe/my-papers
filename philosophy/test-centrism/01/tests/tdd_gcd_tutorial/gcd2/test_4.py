from src.tdd_gcd_tutorial.gcd2 import gcd2

def test_t1():
    assert gcd2(1, 1) == 1

def test_t2():
    assert gcd2(3, 1) == 1

def test_t3():
    assert gcd2(24, 8) == 8

def test_t4():
    assert gcd2(8, 24) == 8
