from src.tdd_gcd_tutorial.gcd8 import gcd8

def test_t1():
    assert gcd8(1, 1) == 1

def test_t2():
    assert gcd8(3, 1) == 1

def test_t3():
    assert gcd8(24, 8) == 8

def test_t4():
    assert gcd8(8, 24) == 8

def test_t5():
    assert gcd8(24, 16) == 8

def test_t6():
    assert gcd8(24, 7) == 1
