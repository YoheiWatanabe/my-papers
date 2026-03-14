from src.tdd_gcd_tutorial.gcd7 import gcd7

def test_t1():
    assert gcd7(1, 1) == 1

def test_t2():
    assert gcd7(3, 1) == 1

def test_t3():
    assert gcd7(24, 8) == 8

def test_t4():
    assert gcd7(8, 24) == 8

def test_t5():
    assert gcd7(24, 16) == 8

def test_t6():
    assert gcd7(24, 7) == 1
