from src.tdd_gcd_tutorial.gcd3 import gcd3

def test_t1():
    assert gcd3(1, 1) == 1

def test_t2():
    assert gcd3(3, 1) == 1

def test_t3():
    assert gcd3(24, 8) == 8

def test_t4():
    assert gcd3(8, 24) == 8
