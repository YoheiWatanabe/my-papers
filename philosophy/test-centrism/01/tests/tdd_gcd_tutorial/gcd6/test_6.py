from src.tdd_gcd_tutorial.gcd6 import gcd6

def test_t1():
    assert gcd6(1, 1) == 1

def test_t2():
    assert gcd6(3, 1) == 1

def test_t3():
    assert gcd6(24, 8) == 8

def test_t4():
    assert gcd6(8, 24) == 8

def test_t5():
    assert gcd6(24, 16) == 8

def test_t6():
    assert gcd6(24, 7) == 1
