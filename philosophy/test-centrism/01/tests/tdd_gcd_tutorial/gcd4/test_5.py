from src.tdd_gcd_tutorial.gcd4 import gcd4

def test_t1():
    assert gcd4(1, 1) == 1

def test_t2():
    assert gcd4(3, 1) == 1

def test_t3():
    assert gcd4(24, 8) == 8

def test_t4():
    assert gcd4(8, 24) == 8

def test_t5():
    assert gcd4(24, 16) == 8
