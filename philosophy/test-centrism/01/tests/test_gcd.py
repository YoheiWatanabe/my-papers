import pytest
from gcd import gcd1, gcd2, gcd3, gcd4, gcd5, gcd6, gcd7

tests = [
        (1, 1, 1),      # a = b & gcd = 1
        (8, 8, 8),      # a = b & gcd > 1
        (24, 1, 1),     # a > b & gcd = 1
        (24, 7, 1),     # a > b & gcd = 1
        (24, 8, 8),     # a > b & gcd > 1
        (24, 16, 8),    # a > b & gcd > 1
        # (24, 14, 2),    # a > b & gcd > 1
        (1, 24, 1),     # a < b & gcd = 1
        (7, 24, 1),     # a < b & gcd = 1
        (8, 24, 8),     # a < b & gcd > 1
        (16, 24, 8),    # a < b & gcd > 1
        # (14, 24, 2),    # a < b & gcd > 1
]

@pytest.mark.parametrize("a,b,expected", tests)
@pytest.mark.parametrize(
    "func",
    [
        pytest.param(gcd1, id="gcd1"),
        pytest.param(gcd2, id="gcd2"),
        pytest.param(gcd3, id="gcd3"),
        pytest.param(gcd4, id="gcd4"),
        pytest.param(gcd5, id="gcd5"),
        pytest.param(gcd6, id="gcd6"),
        pytest.param(gcd7, id="gcd7"),
    ],
)
def test_gcd(func, a, b, expected):
    assert func(a, b) == expected
