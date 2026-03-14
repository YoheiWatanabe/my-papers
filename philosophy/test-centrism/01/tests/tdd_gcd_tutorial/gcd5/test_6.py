from src.tdd_gcd_tutorial.gcd5 import gcd5

def test_t1():
    assert gcd5(1, 1) == 1

def test_t2():
    assert gcd5(3, 1) == 1

def test_t3():
    assert gcd5(24, 8) == 8

def test_t4():
    assert gcd5(8, 24) == 8

def test_t5():
    assert gcd5(24, 16) == 8

def test_t6():
    assert gcd5(24, 7) == 1
